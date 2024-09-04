#!/usr/bin/env python3
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
from Gaudi.Configuration import INFO
from Configurables import MarlinProcessorWrapper, k4DataSvc, GeoSvc
from k4FWCore.parseArgs import parser
from k4MarlinWrapper.inputReader import create_reader, attach_edm4hep2lcio_conversion


parser.add_argument(
    "--inputFiles",
    action="extend",
    nargs="+",
    metavar=["file1", "file2"],
    help="One or multiple input files",
)

parser.add_argument(
    "--compactFile",
    help="Compact detector file to use",
    type=str,
    default=os.environ["K4GEO"] + "/FCCee/CLD/compact/CLD_o2_v07/CLD_o2_v07.xml"
)

parser.add_argument(
    "--drawSecondaries",
    action="store_true",
    help="Enable drawing of secondary MCParticles",
    default=False
)

reco_args = parser.parse_known_args()[0]

algList = []
svcList = []

evtsvc = k4DataSvc("EventDataSvc")
svcList.append(evtsvc)


geoSvc = GeoSvc("GeoSvc")
geoSvc.detectors = [reco_args.compactFile]
geoSvc.OutputLevel = INFO
geoSvc.EnableGeant4Geo = False
svcList.append(geoSvc)


if reco_args.inputFiles:
    read = create_reader(reco_args.inputFiles, evtsvc)
    read.OutputLevel = INFO
    algList.append(read)
else:
    read = None

MyCEDViewer = MarlinProcessorWrapper("MyCEDViewer")
MyCEDViewer.OutputLevel = INFO
MyCEDViewer.ProcessorType = "DDCEDViewer"
MyCEDViewer.Parameters = {
                          "ColorByEnergy": ["false"],
                          "ColorByEnergyAutoColor": ["false"],
                          "ColorByEnergyBrightness": ["1.0"],
                          "ColorByEnergyMax": ["35.0"],
                          "ColorByEnergyMin": ["0.0"],
                          "ColorByEnergySaturation": ["1.0"],
                          "ColorScheme": ["10"],
                          "DetailledDrawing": ["VXD", "VertexBarrel"],
                          "DrawDetector": ["true"],
                          "DrawDetectorID": ["0"],
                          "DrawHelixForPFOs": ["0"],
                          "DrawHelixForTrack": ["0"],
                          "DrawMCParticlesCreatedInSimulation": ["true" if reco_args.drawSecondaries else "false"],
                          "DrawInLayer": [
                              "VXDCollection", "0", "5", "1",
                              "SITCollection", "0", "5", "1",
                              "FTD_PIXELCollection", "0", "5", "1",
                              "FTD_STRIPCollection", "0", "5", "1",
                              "FTDCollection", "0", "5", "1",
                              "TPCCollection", "0", "3", "1",
                              "SETCollection", "0", "3", "1",
                              "ETDCollection", "0", "3", "1",
                              "VertexBarrelCollection", "0", "5", "1",
                              "VertexEndcapCollection", "0", "5", "1",
                              "InnerTrackerBarrelCollection", "0", "5", "1",
                              "InnerTrackerEndcapCollection", "0", "5", "1",
                              "OuterTrackerBarrelCollection", "0", "5", "1",
                              "OuterTrackerEndcapCollection", "0", "5", "1",
                              "VXDTrackerHits", "0", "5", "11",
                              "SITTrackerHits", "0", "5", "11",
                              "TPCTrackerHits", "0", "5", "11",
                              "FTDTrackerHits", "0", "5", "11",
                              "FTDStripTrackerHits", "0", "5", "11",
                              "FTDPixelTrackerHits", "0", "5", "11",
                              "FTDSpacePoints", "0", "5", "11",
                              "SETTrackerHits", "0", "5", "11",
                              "ITrackerEndcapHits", "0", "5", "11",
                              "ITrackerHits", "0", "5", "11",
                              "OTrackerEndcapHits", "0", "5", "11",
                              "OTrackerHits", "0", "5", "11",
                              "VXDEndcapTrackerHits", "0", "5", "11",
                              "LHcalCollection", "0", "3", "2",
                              "LumiCalCollection", "0", "3", "2",
                              "MuonBarrelCollection", "0", "3", "2",
                              "MuonEndCapCollection", "0", "3", "2",
                              "EcalBarrelSiliconCollection", "0", "3", "2",
                              "EcalBarrelSiliconPreShower", "0", "3", "2",
                              "EcalEndcapRingCollection", "0", "3", "2",
                              "EcalEndcapRingPreShower", "0", "3", "2",
                              "EcalEndcapSiliconCollection", "0", "3", "2",
                              "EcalEndcapSiliconPreShower", "0", "3", "2",
                              "HcalBarrelRegCollection", "0", "3", "2",
                              "HcalEndCapRingCollection", "0", "3", "2",
                              "HcalEndCapsCollection", "0", "3", "2",
                              "HcalEndcapRingCollection", "0", "3", "2",
                              "HcalEndcapsCollection", "0", "3", "2",
                              "ECalBarrelSiHitsEven", "0", "3", "2",
                              "ECalBarrelSiHitsOdd", "0", "3", "2",
                              "ECalEndcapSiHitsEven", "0", "3", "2",
                              "ECalEndcapSiHitsOdd", "0", "3", "2",
                              "EcalBarrelCollection", "0", "3", "2",
                              "EcalEndcapsCollection", "0", "3", "2",
                              "YokeEndcapsCollection", "0", "3", "2",
                              "ECalBarrelCollection", "0", "3", "2",
                              "ECalEndcapCollection", "0", "3", "2",
                              "ECalPlugCollection", "0", "3", "2",
                              "EcalBarrelCollection", "0", "3", "2",
                              "EcalEndcapCollection", "0", "3", "2",
                              "EcalPlugCollection", "0", "3", "2",
                              "HCalBarrelCollection", "0", "3", "2",
                              "HCalEndcapCollection", "0", "3", "2",
                              "HCalRingCollection", "0", "3", "2",
                              "YokeBarrelCollection", "0", "3", "2",
                              "YokeEndcapCollection", "0", "3", "2",
                              "LumiCalCollection", "0", "3", "2",
                              "BeamCalCollection", "0", "3", "2",
                              "HCALEndcap", "0", "5", "12",
                              "HCALOther", "0", "5", "12",
                              "MUON", "0", "2", "12",
                              "LHCAL", "0", "3", "12",
                              "LCAL", "0", "3", "12",
                              "BCAL", "0", "3", "12",
                              "ECALBarrel", "0", "2", "12",
                              "ECALEndcap", "0", "2", "12",
                              "ECALOther", "0", "2", "12",
                              "HCALBarrel", "0", "5", "12",
                              "EcalBarrelCollectionRec", "0", "5", "12",
                              "EcalEndcapRingCollectionRec", "0", "5", "12",
                              "EcalEndcapsCollectionRec", "0", "5", "12",
                              "HcalBarrelCollectionRec", "0", "5", "12",
                              "HcalEndcapRingCollectionRec", "0", "5", "12",
                              "HcalEndcapsCollectionRec", "0", "5", "12",
                              "TruthTracks", "0", "6", "3",
                              "ForwardTracks", "0", "6", "4",
                              "SiTracks", "0", "6", "5",
                              "ClupatraTracks", "0", "6", "6",
                              "MarlinTrkTracks", "0", "6", "7",
                              "PandoraClusters", "0", "3", "8",
                              "PandoraPFOs", "0", "3", "9",
                              "MCParticle", "0", "3", "0",
                              "VertexBarrelHits", "0", "5", "11",
                              "VertexEndcapHits", "0", "5", "11",
                              "InnerTrackerBarrelHits", "0", "5", "11",
                              "InnerTrackerEndcapHits", "0", "5", "11",
                              "OuterTrackerBarrelHits", "0", "5", "11",
                              "OuterTrackerEndcapHits", "0", "5", "11",
                              "ECalBarrelHits", "0", "3", "12",
                              "ECalEndcapHits", "0", "3", "12",
                              "ECalPlugHits", "0", "3", "12",
                              "HCalBarrelHits", "0", "3", "12",
                              "HCalEndcapHits", "0", "3", "12",
                              "HCalRingHits", "0", "3", "12",
                              "YokeBarrelHits", "0", "3", "12",
                              "YokeEndcapHits", "0", "3", "12",
                              "LumiCalHits", "0", "3", "12",
                              "BeamCalHits", "0", "3", "12",
                              "Tracks", "0", "3", "3",
                              "SelectedPandoraPFOCollection", "0", "3", "4",
                              "LooseSelectedPandoraPFOCollection", "0", "3", "5",
                              "TightSelectedPandoraPFOCollection", "0", "3", "6",
                              "PandoraPFOCollection", "0", "3", "7",
                              "JetOut", "0", "0", "3"],
                          "DrawSurfaces": ["false"],
                          "HelixMaxR": ["2000"],
                          "HelixMaxZ": ["2500"],
                          "MCParticleEnergyCut": ["0.1"],
                          "ScaleLineThickness": ["1"],
                          "ScaleMarkerSize": ["1"],
                          "UseColorForHelixTracks": ["1"],
                          "UseTrackerExtentForLimitsOfHelix": ["true"],
                          "UsingParticleGun": ["false"],
                          "WaitForKeyboard": ["1"],
                          }

algList.append(MyCEDViewer)

# We need to convert the inputs in case we have EDM4hep input
attach_edm4hep2lcio_conversion(algList, read)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax = 10,
                ExtSvc = svcList,
                OutputLevel = INFO
              )
