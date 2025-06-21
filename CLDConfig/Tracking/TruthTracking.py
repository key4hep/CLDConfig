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
args = parser.parse_known_args()

truth_track_finder_args = {
    "FitForward": True,
    "MCParticleCollectionName": ["MCParticle"],
    "SiTrackCollectionName": ["SiTracks"],
    "SiTrackRelationCollectionName": ["SiTrackRelations"],
    "SimTrackerHitRelCollectionNames": ["VXDTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations"],
    "TrackerHitCollectionNames": ["VXDTrackerHits", "ITrackerHits", "OTrackerHits", "VXDEndcapTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
    "UseTruthInPrefit": False,
}
# Change True to ["true"] and False to ["false"] if using MarlinProcessorWrapper
truth_track_finder_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in truth_track_finder_args.items()}

if args[0].native:
    from Configurables import TruthTrackFinder
    MyTruthTrackFinder = TruthTrackFinder(
        "TruthTrackFinder",
        **truth_track_finder_args,
        OutputLevel=WARNING,
    )

else:
    from Configurables import MarlinProcessorWrapper

    MyTruthTrackFinder = MarlinProcessorWrapper("MyTruthTrackFinder")
    MyTruthTrackFinder.OutputLevel = WARNING
    MyTruthTrackFinder.ProcessorType = "TruthTrackFinder"
    MyTruthTrackFinder.Parameters = truth_track_finder_args_marlin

TruthTrackingSequence = [
    MyTruthTrackFinder,
]
