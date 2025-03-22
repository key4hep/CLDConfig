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
from Configurables import MarlinProcessorWrapper


# geoservice comes from the `global_vars` of the SequenceLoader
if any(small_vtx in geoservice.detectors[0] for small_vtx in ["_o2_", "_o3_", "_o4_"]):
    CT_MAX_DIST = "0.05;"  # semi-colon is important!
elif "_o1_" in  geoservice.detectors[0]:
    CT_MAX_DIST = "0.03;"  # semi-colon is important!
else:
    raise RuntimeError("Unknown detector model to chose CT_MAX_DISTANCE")

from k4FWCore.parseArgs import parser
args = parser.parse_known_args()

collections = [
    ["VXDTrackerHits"],
    ["VXDEndcapTrackerHits"],
    ["VXDTrackerHits", "VXDEndcapTrackerHits"],
    [],
    ["ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
    [
        "VXDTrackerHits",
        "VXDEndcapTrackerHits",
        "ITrackerHits",
        "OTrackerHits",
        "ITrackerEndcapHits",
        "OTrackerEndcapHits",
    ],
]
params = [
    [
        "MaxCellAngle",
        ":",
        "0.01;",
        "MaxCellAngleRZ",
        ":",
        "0.01;",
        "Chi2Cut",
        ":",
        "100;",
        "MinClustersOnTrack",
        ":",
        "4;",
        "MaxDistance",
        ":",
        CT_MAX_DIST,
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "10.0;",
    ],
    [
        "MaxCellAngle",
        ":",
        "0.01;",
        "MaxCellAngleRZ",
        ":",
        "0.01;",
        "Chi2Cut",
        ":",
        "100;",
        "MinClustersOnTrack",
        ":",
        "4;",
        "MaxDistance",
        ":",
        CT_MAX_DIST,
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "10.0;",
    ],
    [
        "MaxCellAngle",
        ":",
        "0.05;",
        "MaxCellAngleRZ",
        ":",
        "0.05;",
        "Chi2Cut",
        ":",
        "100;",
        "MinClustersOnTrack",
        ":",
        "4;",
        "MaxDistance",
        ":",
        CT_MAX_DIST,
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "10.0;",
    ],
    [
        "MaxCellAngle",
        ":",
        "0.1;",
        "MaxCellAngleRZ",
        ":",
        "0.1;",
        "Chi2Cut",
        ":",
        "2000;",
        "MinClustersOnTrack",
        ":",
        "4;",
        "MaxDistance",
        ":",
        CT_MAX_DIST,
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "10.0;",
    ],
    [
        "MaxCellAngle",
        ":",
        "0.1;",
        "MaxCellAngleRZ",
        ":",
        "0.1;",
        "Chi2Cut",
        ":",
        "2000;",
        "MinClustersOnTrack",
        ":",
        "4;",
        "MaxDistance",
        ":",
        CT_MAX_DIST,
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "1.0;",
    ],
    [
        "MaxCellAngle",
        ":",
        "0.1;",
        "MaxCellAngleRZ",
        ":",
        "0.1;",
        "Chi2Cut",
        ":",
        "1000;",
        "MinClustersOnTrack",
        ":",
        "5;",
        "MaxDistance",
        ":",
        "0.015;",
        "SlopeZRange",
        "10.0;",
        "HighPTCut",
        "10.0;",
    ],
]
flags = [
    ["HighPTFit", "VertexToTracker"],
    ["HighPTFit", "VertexToTracker"],
    ["HighPTFit", "VertexToTracker", "RadialSearch"],
    ["HighPTFit", "VertexToTracker", "RadialSearch"],
    ["HighPTFit", "VertexToTracker", "RadialSearch"],
    ["OnlyZSchi2cut", "RadialSearch"],
]
functions = [
    [
        "CombineCollections",
        "BuildNewTracks",
    ],
    [
        "CombineCollections",
        "ExtendTracks",
    ],
    [
        "CombineCollections",
        "BuildNewTracks",
    ],
    [
        "BuildNewTracks",
        "SortTracks",
    ],
    [
        "CombineCollections",
        "ExtendTracks",
    ],
    [
        "CombineCollections",
        "BuildNewTracks",
    ],
]

names = []
values = []
for ls in params:
    current_names = []
    current_values = []
    ls = [x for x in ls if x != ":"]
    for i in range(0, len(ls), 2):
        current_names.append(ls[i])
        current_values.append(float(ls[i + 1].replace(";", "")))
    names.append(current_names)
    values.append(current_values)

conformal_tracking_args = {
    "DebugHits": ["DebugHits"],
    "DebugPlots": False,
    "DebugTiming": False,
    "MCParticleCollectionName": ["MCParticle"],
    "MaxHitInvertedFit": 0,
    "MinClustersOnTrackAfterFit": 3,
    "RelationsNames": ["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
    "RetryTooManyTracks": False,
    "SiTrackCollectionName": ["SiTracksCT"],
    "SortTreeResults": True,
    "Steps":
    [
        "[VXDBarrel]",
        "@Collections", ":", "VXDTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker",
        "@Functions", ":", "CombineCollections,", "BuildNewTracks",
        "[VXDEncap]",
        "@Collections", ":", "VXDEndcapTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.01;", "MaxCellAngleRZ", ":", "0.01;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker",
        "@Functions", ":", "CombineCollections,", "ExtendTracks",
        "[LowerCellAngle1]",
        "@Collections", ":", "VXDTrackerHits,", "VXDEndcapTrackerHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.05;", "MaxCellAngleRZ", ":", "0.05;", "Chi2Cut", ":", "100;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch",
        "@Functions", ":", "CombineCollections,", "BuildNewTracks",
        "[LowerCellAngle2]",
        "@Collections", ":",
        "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch",
        "@Functions", ":", "BuildNewTracks,", "SortTracks",
        "[Tracker]",
        "@Collections", ":", "ITrackerHits,", "OTrackerHits,", "ITrackerEndcapHits,", "OTrackerEndcapHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "2000;", "MinClustersOnTrack", ":", "4;", "MaxDistance", ":", CT_MAX_DIST, "SlopeZRange:", "10.0;", "HighPTCut:", "1.0;",
        "@Flags", ":", "HighPTFit,", "VertexToTracker,", "RadialSearch",
        "@Functions", ":", "CombineCollections,", "ExtendTracks",
        "[Displaced]",
        "@Collections", ":", "VXDTrackerHits,", "VXDEndcapTrackerHits,", "ITrackerHits,", "OTrackerHits,", "ITrackerEndcapHits,", "OTrackerEndcapHits",
        "@Parameters", ":", "MaxCellAngle", ":", "0.1;", "MaxCellAngleRZ", ":", "0.1;", "Chi2Cut", ":", "1000;", "MinClustersOnTrack", ":", "5;", "MaxDistance", ":", "0.015;", "SlopeZRange:", "10.0;", "HighPTCut:", "10.0;",
        "@Flags", ":", "OnlyZSchi2cut,", "RadialSearch",
        "@Functions", ":", "CombineCollections,", "BuildNewTracks"
    ],
    "ThetaRange": 0.05,
    "TooManyTracks": 100000,
    "TrackerHitCollectionNames": ["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
    "trackPurity": 0.7
}

conformal_tracking_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in conformal_tracking_args.items()}
conformal_tracking_args_marlin = {k: [str(v)] if isinstance(v, float) or isinstance(v, int) else v for k, v in conformal_tracking_args_marlin.items()}

conformal_tracking_args.pop("Steps")
conformal_tracking_args["stepCollections"] = collections
conformal_tracking_args["stepParametersNames"] = names
conformal_tracking_args["stepParametersValues"] = values
conformal_tracking_args["stepParametersFlags"] = flags
conformal_tracking_args["stepParametersFunctions"] = functions

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
