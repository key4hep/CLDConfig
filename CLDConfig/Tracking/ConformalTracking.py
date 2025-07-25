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
from Gaudi.Configuration import WARNING
from k4FWCore.parseArgs import parser

from conformal_tracking_utils import configure_conformal_tracking_steps

# geoservice comes from the `global_vars` of the SequenceLoader
if any(small_vtx in geoservice.detectors[0] for small_vtx in ["_o2_", "_o3_", "_o4_"]):
    CT_MAX_DIST = 0.05
elif "_o1_" in  geoservice.detectors[0]:
    CT_MAX_DIST = 0.03
else:
    raise RuntimeError("Unknown detector model to chose CT_MAX_DISTANCE")

args = parser.parse_known_args()

# The keys are simply a name are not passed to ConformalTracking
parameters = {
        "VXDBarrel": {
            "collections": ["VXDTrackerHits"],
            "params": {
                "MaxCellAngle": 0.01,
                "MaxCellAngleRZ": 0.01,
                "Chi2Cut": 100,
                "MinClustersOnTrack": 4,
                "MaxDistance": CT_MAX_DIST,
                "SlopeZRange": 10.0,
                "HighPTCut": 10.0,
            },
            "flags": ["HighPTFit", "VertexToTracker"],
            "functions": ["CombineCollections", "BuildNewTracks"],
        },
        "VXDEncap": {
            "collections": ["VXDEndcapTrackerHits"],
            "params": {
                "MaxCellAngle": 0.01,
                "MaxCellAngleRZ": 0.01,
                "Chi2Cut": 100,
                "MinClustersOnTrack": 4,
                "MaxDistance": CT_MAX_DIST,
                "SlopeZRange": 10.0,
                "HighPTCut": 10.0,
            },
            "flags": ["HighPTFit", "VertexToTracker"],
            "functions": ["CombineCollections", "ExtendTracks"],
        },
        "LowerCellAngle1": {
            "collections": ["VXDTrackerHits", "VXDEndcapTrackerHits"],
            "params": {
                "MaxCellAngle": 0.05,
                "MaxCellAngleRZ": 0.05,
                "Chi2Cut": 100,
                "MinClustersOnTrack": 4,
                "MaxDistance": CT_MAX_DIST,
                "SlopeZRange": 10.0,
                "HighPTCut": 10.0,
            },
            "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
            "functions": ["CombineCollections", "BuildNewTracks"],
        },
        "LowerCellAngle2": {
            "collections": [],
            "params": {
                "MaxCellAngle": 0.1,
                "MaxCellAngleRZ": 0.1,
                "Chi2Cut": 2000,
                "MinClustersOnTrack": 4,
                "MaxDistance": CT_MAX_DIST,
                "SlopeZRange": 10.0,
                "HighPTCut": 10.0,
            },
            "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
            "functions": ["BuildNewTracks", "SortTracks"],
        },
        "Tracker": {
            "collections": ["ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
            "params": {
                "MaxCellAngle": 0.1,
                "MaxCellAngleRZ": 0.1,
                "Chi2Cut": 2000,
                "MinClustersOnTrack": 4,
                "MaxDistance": CT_MAX_DIST,
                "SlopeZRange": 10.0,
                "HighPTCut": 1.0,
            },
            "flags": ["HighPTFit", "VertexToTracker", "RadialSearch"],
            "functions": ["CombineCollections", "ExtendTracks"],
        },
        "Displaced": {
            "collections": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
            "params": {
                "MaxCellAngle": 0.1,
                "MaxCellAngleRZ": 0.1,
                "Chi2Cut": 1000,
                "MinClustersOnTrack": 5,
                "MaxDistance": 0.015,
                "SlopeZRange": 10.0,
                "HighPTCut": 10.0,
            },
            "flags": ["OnlyZSchi2cut", "RadialSearch"],
            "functions": ["CombineCollections", "BuildNewTracks"],
        },
    }

steps_marlin = []

for name, param_dict in parameters.items():
    marlin_collections = []
    for i in range(len(param_dict["collections"])):
        marlin_collections.append(f"{param_dict['collections'][i]}")
        if i < len(param_dict["collections"]) - 1:
            marlin_collections[-1] += ","
    marlin_parameters = []
    for i, (k, v) in enumerate(param_dict["params"].items()):
        marlin_parameters.extend([k, ":", f"{v};"])

    marlin_flags = []
    for i in range(len(param_dict["flags"])):
        marlin_flags.append(f"{param_dict['flags'][i]}")
        if i < len(param_dict["flags"]) - 1:
            marlin_flags[-1] += ","
    marlin_functions = []
    for i in range(len(param_dict["functions"])):
        marlin_functions.append(f"{param_dict['functions'][i]}")
        if i < len(param_dict["functions"]) - 1:
            marlin_functions[-1] += ","
    current_step = [
        f"[{name}]",
        "@Collections", ":", *marlin_collections,
        "@Parameters", ":", *marlin_parameters,
        "@Flags", ":", *marlin_flags,
        "@Functions", ":", *marlin_functions,
    ]
    steps_marlin.extend(current_step)

conformal_tracking_args = {
    "DebugHits": ["DebugHits"],
    "DebugPlots": False,
    "DebugTiming": False,
    "MCParticleCollectionName": ["MCParticles"],
    "MaxHitInvertedFit": 0,
    "MinClustersOnTrackAfterFit": 3,
    "RelationsNames": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
    "RetryTooManyTracks": False,
    "SiTrackCollectionName": ["SiTracksCT"],
    "SortTreeResults": True,
    "ThetaRange": 0.05,
    "TooManyTracks": 100000,
    "TrackerHitCollectionNames": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
    "trackPurity": 0.7
}

conformal_tracking_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in conformal_tracking_args.items()}
conformal_tracking_args_marlin = {k: [str(v)] if isinstance(v, float) or isinstance(v, int) else v for k, v in conformal_tracking_args_marlin.items()}
conformal_tracking_args_marlin["MCParticleCollectionName"] = ["MCParticle"]

if args[0].native:
    # Not implemented in Gaudi
    conformal_tracking_args.pop("DebugHits")
else:
    conformal_tracking_args_marlin["Steps"] = steps_marlin

clones_and_split_tracks_finder_args = {
    "EnergyLossOn": True,
    "InputTrackCollectionName": ["SiTracksCT"],
    "MultipleScatteringOn": True,
    "OutputTrackCollectionName": ["SiTracks"],
    "SmoothOn": False,
    "extrapolateForward": True,
    "maxSignificancePhi": 3.,
    "maxSignificancePt": 2.,
    "maxSignificanceTheta": 3.,
    "mergeSplitTracks": False,
    "minTrackPt": 1.,
}

clone_and_split_tracks_finder_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in clones_and_split_tracks_finder_args.items()}
clone_and_split_tracks_finder_args_marlin = {k: [str(v)] if isinstance(v, float) else v for k, v in clone_and_split_tracks_finder_args_marlin.items()}

if args[0].native:
    from Configurables import ConformalTracking, ClonesAndSplitTracksFinder

    MyConformalTracking = ConformalTracking(
        "ConformalTracking",
        **conformal_tracking_args,
        OutputLevel=WARNING,
    )
    configure_conformal_tracking_steps(MyConformalTracking, parameters)

    clones_and_split_tracks_finder = ClonesAndSplitTracksFinder(
        "ClonesAndSplitTracksFinder",
        **clones_and_split_tracks_finder_args,
        OutputLevel=WARNING,
    )

else:
    from Configurables import MarlinProcessorWrapper
    MyConformalTracking = MarlinProcessorWrapper("MyConformalTracking")
    MyConformalTracking.OutputLevel = WARNING
    MyConformalTracking.ProcessorType = "ConformalTrackingV2"
    MyConformalTracking.Parameters = conformal_tracking_args_marlin

    clones_and_split_tracks_finder = MarlinProcessorWrapper("ClonesAndSplitTracksFinder")
    clones_and_split_tracks_finder.OutputLevel = WARNING
    clones_and_split_tracks_finder.ProcessorType = "ClonesAndSplitTracksFinder"
    clones_and_split_tracks_finder.Parameters = clone_and_split_tracks_finder_args_marlin

ConformalTrackingSequence = [
    MyConformalTracking,
    clones_and_split_tracks_finder,
]
