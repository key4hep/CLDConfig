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
# ACTS based track finding and fitting from k4ActsTracking. Needs the ActsGeoSvc
# which is set up in CLDReconstruction.py when --tracking=acts is used.
#
# NOTE: The seeding and CKF parameters are taken from the technical test in
# k4ActsTracking (test/options/CLD_CKFTracking.py) and are not tuned for CLD yet
from Gaudi.Configuration import WARNING
from Configurables import CollectionMerger, CKFTrackingAlg, ACTSDuplicateRemoval

# The CKF takes a single hit collection, so merge all tracker hits (and their
# relations, which are a required input) first
MergeTrackerHits = CollectionMerger(
    "MergeTrackerHits",
    InputCollections=["VXDTrackerHits", "VXDEndcapTrackerHits", "ITrackerHits", "OTrackerHits", "ITrackerEndcapHits", "OTrackerEndcapHits"],
    OutputCollection="AllTrackerHits",
    OutputLevel=WARNING,
)

MergeTrackerHitRelations = CollectionMerger(
    "MergeTrackerHitRelations",
    InputCollections=["VXDTrackerHitRelations", "VXDEndcapTrackerHitRelations", "InnerTrackerBarrelHitsRelations", "InnerTrackerEndcapHitsRelations", "OuterTrackerBarrelHitsRelations", "OuterTrackerEndcapHitsRelations"],
    OutputCollection="AllTrackerHitRelations",
    OutputLevel=WARNING,
)

ckf_tracking_args = {
    "RunCKF": True,
    # Seeds are built from the VXD (barrel and endcap; system 1|2) and the first
    # inner tracker layer (barrel and endcap; system 3|4)
    "SeedingSensorsCellIDs": ["system:1|2", "system:3|4,layer:1"],
    # TODO: tune for CLD
    "SeedFinding_RMax": 150,
    "SeedFinding_MinPt": 500,
    "SeedFinding_ImpactMax": 3,
    "SeedFinding_SigmaScattering": 50,
    "SeedFinding_CollisionRegion": 6,
    "SeedFinding_RadLengthPerSeed": 0.1,
    "CKF_Chi2CutOff": 10,
    "CKF_NumMeasurementsCutOff": 1,
    # Pandora needs the AtCalorimeter track state
    "ExtrapolateToCalo": True,
    "InputTrackerHitCollection": MergeTrackerHits.OutputCollection,
    "InputTrackerHitRelationCollection": MergeTrackerHitRelations.OutputCollection,
    "OutputSeedCollection": "SiTrackSeedsCKF",
    "OutputTrackCollection": "SiTracksCKF",
}

MyCKFTracking = CKFTrackingAlg(
    "CKFTracking",
    **ckf_tracking_args,
    OutputLevel=WARNING,
)

MyACTSDuplicateRemoval = ACTSDuplicateRemoval(
    "ACTSDuplicateRemoval",
    InputTrackCollectionName=[MyCKFTracking.OutputTrackCollection],
    OutputTrackCollectionName=["SiTracks"],
    OutputLevel=WARNING,
)

ActsTrackingSequence = [
    MergeTrackerHits,
    MergeTrackerHitRelations,
    MyCKFTracking,
    MyACTSDuplicateRemoval,
]
