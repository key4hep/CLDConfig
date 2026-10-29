#
# Copyright (c) 2014-2024 Key4hep-Project.
#
# This file is part of Key4hep.
# See https://key4hep.github.io/key4hep-doc/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from Gaudi.Configuration import INFO, WARNING, DEBUG

from Gaudi.Configurables import EventDataSvc, MarlinProcessorWrapper, GeoSvc, TrackingCellIDEncodingSvc
from k4FWCore import ApplicationMgr, IOSvc
from k4FWCore.parseArgs import parser
import sys
base_dir = os.path.dirname(__file__)
sys.path.append(base_dir)
from py_utils import SequenceLoader, parse_collection_patch_file
from k4MarlinWrapper.io_helpers import IOHandlerHelper
from Configurables import GeoSvc, TrackingCellIDEncodingSvc

parser_group = parser.add_argument_group("CLDReconstruction.py custom options")
# Need the dummy input such that the IOHandlerHelper.add_reader call below does not crash when called with --help
parser_group.add_argument("--inputFiles", action="store", nargs="+", metavar=("file1", "file2"), help="One or multiple input files", default=["dummy_input.edm4hep.root"])
parser_group.add_argument("--outputBasename", help="Basename of the output file(s)", default="output")
parser_group.add_argument("--trackingOnly", action="store_true", help="Run only track reconstruction", default=False)
parser_group.add_argument("--enableLCFIJet", action="store_true", help="Enable LCFIPlus jet clustering parts", default=False)
parser_group.add_argument("--enableMLJetTagger", action="store_true", help="Enable ML-based jet flavor tagging", default=False)
parser_group.add_argument("--MLJetTaggerModel", action="store", help="Type of ML model to use for inference", type=str, default="model_ParT_ecm240_cld_o2_v5")
parser_group.add_argument("--cms", action="store", help="Choose a Centre-of-Mass energy", default=240, choices=(91, 160, 240, 365), type=int)
parser_group.add_argument("--compactFile", help="Compact detector file to use", type=str, default=os.environ["K4GEO"] + "/FCCee/CLD/compact/CLD_o2_v07/CLD_o2_v07.xml")
parser_group.add_argument("--native", action="store_true", help="Use the native EDM4hep tracking", default=False)
tracking_group = parser_group.add_mutually_exclusive_group()
tracking_group.add_argument("--conformalTracking", action="store_true", default=True, help="Use conformal tracking pattern recognition")
tracking_group.add_argument("--truthTracking", action="store_true", default=False, help="Cheat tracking pattern recognition")
parser_group.add_argument("--calorimeterIntegrationTimeWindow", help="Calorimeter integration time window", default="10ns", choices=("10ns", "400ns"))
# "Skip" removes the overlay processor completely. This is used to create the wrapped reference for the
# native EDM4hep reconstruction, which does not run the overlay, so that both outputs can be compared
parser_group.add_argument("--overlay", help="Background overlay to use, 'Skip' does not run the overlay processor (nor the RecoMCTruthLink that depends on it)", default="False", choices=("False", "91GeV", "365GeV", "Skip"))
parser_group.add_argument("--vertexUnconstrained", action="store_true", help="Also run the unconstrained vertex finder", default=False)
parser_group.add_argument("--outputMode", help="Output file format", default="EDM4hep", choices=("LCIO", "EDM4hep"))
reco_args = parser.parse_known_args()[0]

if reco_args.native and reco_args.outputMode == "LCIO":
    parser.error("LCIO output is not supported with --native")

# Decide here which stages run, such that the sequence below only needs to check a single flag.
# Stages without a native implementation (yet) only run in the wrapped Marlin flow
run_overlay = not reco_args.native and reco_args.overlay != "Skip"
# needs the MCPhysicsParticles created by the overlay processor
run_mc_truth_link = run_overlay
run_diagnostics = not reco_args.native
run_calo = not reco_args.trackingOnly
run_high_level_reco = run_calo and not reco_args.native


evtsvc = EventDataSvc("EventDataSvc")
iosvc = IOSvc()
svcList = [evtsvc, iosvc]
algList = []

REC_COLLECTION_CONTENTS_FILE = f"{base_dir}/collections_rec_level.txt" # file with the collections to be patched in when writing from LCIO to EDM4hep

geoservice = GeoSvc("GeoSvc")
geoservice.detectors = [reco_args.compactFile]
geoservice.OutputLevel = INFO
geoservice.EnableGeant4Geo = False
svcList.append(geoservice)

# Luminous region (vertex) sizes (sigma_x, sigma_y, sigma_z) in mm, derived from the IP beam sizes
# sigma_x*, sigma_y* and the bunch length sigma_z (incl. beamstrahlung) given in Table 2 of the
# FCC Feasibility Study Report Vol. 2 (2025), https://arxiv.org/abs/2505.00274, with a half crossing
# angle alpha = 15 mrad, following
# https://github.com/HEP-FCC/FCCeePhysicsPerformance/blob/d6ecee2c2c3ed5d76db55a3ae18ced349b2b914a/General/README.md:
#   vertex sigma_x = sigma_x* / sqrt(2)
#   vertex sigma_y = sigma_y* / sqrt(2)
#   vertex sigma_z = 1 / sqrt(2 sin^2(alpha) / sigma_x*^2 + 2 cos^2(alpha) / sigma_z^2)
BEAM_SPOT_SIZES = { 91:  (6.36e-3,  28.3e-6, 0.424),
                    160: (15.56e-3, 31.8e-6, 1.00),
                    240: (9.19e-3,  22.6e-6, 0.606),
                    365: (26.16e-3, 31.1e-6, 1.20),
                   }

sequenceLoader = SequenceLoader(
    algList,
    # global_vars can be used in sequence-loaded modules without explicit import
    global_vars={"geoservice": geoservice, "reco_args": reco_args,
                 "BEAM_SPOT_SIZES": BEAM_SPOT_SIZES,
                 },
    base_dir=base_dir,
)

if reco_args.native:
    iosvc.Input = reco_args.inputFiles
    iosvc.Output = f"{reco_args.outputBasename}_REC.edm4hep.root"
else:
    cellIDSvc = TrackingCellIDEncodingSvc("CellIDSvc")
    cellIDSvc.EncodingStringParameterName = "GlobalTrackerReadoutID"
    cellIDSvc.GeoSvcName = geoservice.name()
    cellIDSvc.OutputLevel = INFO
    svcList.append(cellIDSvc)

    io_handler = IOHandlerHelper(algList, iosvc)
    io_handler.add_reader(reco_args.inputFiles)

    MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
    MyAIDAProcessor.OutputLevel = WARNING
    MyAIDAProcessor.ProcessorType = "AIDAProcessor"
    MyAIDAProcessor.Parameters = {
                                  "Compress": ["1"],
                                  "FileName": [f"{reco_args.outputBasename}_aida"],
                                  "FileType": ["root"]
                                  }

    EventNumber = MarlinProcessorWrapper("EventNumber")
    EventNumber.OutputLevel = WARNING
    EventNumber.ProcessorType = "Statusmonitor"
    EventNumber.Parameters = {
                              "HowOften": ["1"]
                              }

    # setup AIDA histogramming
    algList.append(MyAIDAProcessor)
    algList.append(EventNumber)

# background overlay
if run_overlay:
    sequenceLoader.load("Overlay/Overlay")
# tracker hit digitisation
sequenceLoader.load("Tracking/TrackingDigi")

# tracking
if reco_args.truthTracking:
    sequenceLoader.load("Tracking/TruthTracking")
elif reco_args.conformalTracking:
    sequenceLoader.load("Tracking/ConformalTracking")

sequenceLoader.load("Tracking/Refit")

# calorimeter digitization and pandora
if run_calo:
    sequenceLoader.load("CaloDigi/CaloDigi")
    sequenceLoader.load("CaloDigi/MuonDigi")
    sequenceLoader.load("ParticleFlow/Pandora")
    sequenceLoader.load("CaloDigi/LumiCal")
# Reco to MCTruth linking
if run_mc_truth_link:
    sequenceLoader.load("HighLevelReco/RecoMCTruthLink")
# monitoring
if run_diagnostics:
    sequenceLoader.load("Diagnostics/Tracking")
# pfo selector (might need re-optimisation)
if run_high_level_reco:
    sequenceLoader.load("HighLevelReco/PFOSelector")
    sequenceLoader.load("HighLevelReco/JetClusteringOrRenaming")
    sequenceLoader.load("HighLevelReco/JetAndVertex")
    sequenceLoader.load("HighLevelReco/MLJetTagger")

DST_KEEPLIST = ["MCParticlesSkimmed", "MCPhysicsParticles", "RecoMCTruthLink", "SiTracks", "SiTracks_Refitted", "PandoraClusters", "PandoraPFOs", "SelectedPandoraPFOs", "LooseSelectedPandoraPFOs", "TightSelectedPandoraPFOs", "RefinedVertexJets", "RefinedVertexJets_rel", "RefinedVertexJets_vtx", "RefinedVertexJets_vtx_RP", "BuildUpVertices", "BuildUpVertices_res", "BuildUpVertices_RP", "BuildUpVertices_res_RP", "BuildUpVertices_V0", "BuildUpVertices_V0_res", "BuildUpVertices_V0_RP", "BuildUpVertices_V0_res_RP", "PrimaryVertices", "PrimaryVertices_res", "PrimaryVertices_RP", "PrimaryVertices_res_RP", "RefinedVertices", "RefinedVertices_RP"]

DST_SUBSETLIST = ["EfficientMCParticles", "InefficientMCParticles", "MCPhysicsParticles"]

# The native flow writes its output via the IOSvc configured above
if not reco_args.native:
    if reco_args.outputMode == "LCIO":
        Output_REC = io_handler.add_lcio_writer("Output_REC")
        Output_REC.Parameters = {
            "LCIOOutputFile": [f"{reco_args.outputBasename}_REC.slcio"],
            "LCIOWriteMode": ["WRITE_NEW"],
        }

        Output_DST = io_handler.add_lcio_writer("Output_DST")
        dropped_types = ["MCParticle", "LCRelation", "SimCalorimeterHit", "CalorimeterHit", "SimTrackerHit", "TrackerHit", "TrackerHitPlane", "Track", "ReconstructedParticle", "LCFloatVec"]
        Output_DST.Parameters = {
            "LCIOOutputFile": [f"{reco_args.outputBasename}_DST.slcio"],
            "LCIOWriteMode": ["WRITE_NEW"],
            "DropCollectionNames": [],
            "DropCollectionTypes": dropped_types,
            "FullSubsetCollections": DST_SUBSETLIST,
            "KeepCollectionNames": DST_KEEPLIST,
        }

    elif reco_args.outputMode == "EDM4hep":
        # Make sure that all collections are always available by patching in missing ones on-the-fly
        collPatcherRec = MarlinProcessorWrapper(
            "CollPatcherREC", OutputLevel=INFO, ProcessorType="PatchCollections"
        )
        collPatcherRec.Parameters = {
            "PatchCollections": parse_collection_patch_file(REC_COLLECTION_CONTENTS_FILE)
        }
        algList.append(collPatcherRec)

        io_handler.add_edm4hep_writer(f"{reco_args.outputBasename}_REC.edm4hep.root", ["keep *"])
        # FIXME: needs https://github.com/key4hep/k4FWCore/issues/226
        # <DST output for edm4hep>

    # We need to attach all the necessary converters
    io_handler.finalize_converters()


ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax = 3, # Overridden by the --num-events switch to k4run
                ExtSvc = svcList,
                OutputLevel=WARNING
              )
