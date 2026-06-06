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
from Configurables import EventDataSvc
from k4FWCore import ApplicationMgr, IOSvc

svc = IOSvc()
svc.Input = "dummy_input.root"
svc.Output = "dummy_output.root"
svc.outputCommands = [
    # Drop everything by default, then keep only what we want
    "drop *",
    # --- Original simulation collections ---
    "keep ECalBarrelCollection",
    "keep ECalBarrelCollectionContributions",
    "keep ECalEndcapCollection",
    "keep ECalEndcapCollectionContributions",
    "keep EventHeader",
    "keep HCalBarrelCollection",
    "keep HCalBarrelCollectionContributions",
    "keep HCalEndcapCollection",
    "keep HCalEndcapCollectionContributions",
    "keep HCalRingCollection",
    "keep HCalRingCollectionContributions",
    "keep InnerTrackerBarrelCollection",
    "keep InnerTrackerEndcapCollection",
    "keep LumiCalCollection",
    "keep LumiCalCollectionContributions",
    "keep MCParticles",
    "keep OuterTrackerBarrelCollection",
    "keep OuterTrackerEndcapCollection",
    "keep VertexBarrelCollection",
    "keep VertexEndcapCollection",
    "keep YokeBarrelCollection",
    "keep YokeBarrelCollectionContributions",
    "keep YokeEndcapCollection",
    "keep YokeEndcapCollectionContributions",
    # --- TrackingDigi output collections (TrackingDigi.py) ---
    "keep VXDTrackerHits",
    "keep VXDTrackerHitRelations",
    "keep VXDEndcapTrackerHits",
    "keep VXDEndcapTrackerHitRelations",
    "keep ITrackerHits",
    "keep InnerTrackerBarrelHitsRelations",
    "keep ITrackerEndcapHits",
    "keep InnerTrackerEndcapHitsRelations",
    "keep OTrackerHits",
    "keep OuterTrackerBarrelHitsRelations",
    "keep OTrackerEndcapHits",
    "keep OuterTrackerEndcapHitsRelations",
]

ApplicationMgr(
    TopAlg=[],
    EvtSel="NONE",
    EvtMax=-1,
    ExtSvc=[EventDataSvc("EventDataSvc")],
    OutputLevel=WARNING,
)
