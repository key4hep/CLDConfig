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
from Configurables import DDPlanarDigi


VXDBarrelDigitiser = DDPlanarDigi("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = WARNING
VXDBarrelDigitiser.IsStrip = False
VXDBarrelDigitiser.ResolutionU = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003]
VXDBarrelDigitiser.ResolutionV = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003]
VXDBarrelDigitiser.SimTrackHitCollectionName = "VertexBarrelCollection"
VXDBarrelDigitiser.SimTrkHitRelCollection = "VXDTrackerHitRelations"
VXDBarrelDigitiser.SubDetectorName = "Vertex"

VXDEndcapDigitiser = DDPlanarDigi("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = WARNING
VXDEndcapDigitiser.IsStrip = False
VXDEndcapDigitiser.ResolutionU = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003]
VXDEndcapDigitiser.ResolutionV = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003]
VXDEndcapDigitiser.SimTrackHitCollectionName = "VertexEndcapCollection"
VXDEndcapDigitiser.SimTrkHitRelCollection = "VXDEndcapTrackerHitRelations"
VXDEndcapDigitiser.SubDetectorName = "Vertex"
VXDEndcapDigitiser.TrackerHitCollectionName = "VXDEndcapTrackerHits"


InnerPlanarDigiProcessor = DDPlanarDigi("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = WARNING
InnerPlanarDigiProcessor.IsStrip = False
InnerPlanarDigiProcessor.ResolutionU = [0.007]
InnerPlanarDigiProcessor.ResolutionV = [0.09]
InnerPlanarDigiProcessor.SimTrackHitCollectionName = "InnerTrackerBarrelCollection"
InnerPlanarDigiProcessor.SimTrkHitRelCollection = "InnerTrackerBarrelHitsRelations"
InnerPlanarDigiProcessor.SubDetectorName = "InnerTrackers"
InnerPlanarDigiProcessor.TrackerHitCollectionName = "ITrackerHits"

InnerEndcapPlanarDigiProcessor = DDPlanarDigi("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = WARNING
InnerEndcapPlanarDigiProcessor.IsStrip = False
InnerEndcapPlanarDigiProcessor.ResolutionU = [0.005, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007]
InnerEndcapPlanarDigiProcessor.ResolutionV = [0.005, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09]
InnerEndcapPlanarDigiProcessor.SimTrackHitCollectionName = "InnerTrackerEndcapCollection"
InnerEndcapPlanarDigiProcessor.SimTrkHitRelCollection = "InnerTrackerEndcapHitsRelations"
InnerEndcapPlanarDigiProcessor.SubDetectorName = "InnerTrackers"
InnerEndcapPlanarDigiProcessor.TrackerHitCollectionName = "ITrackerEndcapHits"

OuterPlanarDigiProcessor = DDPlanarDigi("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = WARNING
OuterPlanarDigiProcessor.IsStrip = False
OuterPlanarDigiProcessor.ResolutionU = [0.007, 0.007, 0.007]
OuterPlanarDigiProcessor.ResolutionV = [0.09, 0.09, 0.09]
OuterPlanarDigiProcessor.SimTrackHitCollectionName = "OuterTrackerBarrelCollection"
OuterPlanarDigiProcessor.SimTrkHitRelCollection = "OuterTrackerBarrelHitsRelations"
OuterPlanarDigiProcessor.SubDetectorName = "OuterTrackers"
OuterPlanarDigiProcessor.TrackerHitCollectionName = "OTrackerHits"

OuterEndcapPlanarDigiProcessor = DDPlanarDigi("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = WARNING
OuterEndcapPlanarDigiProcessor.IsStrip = False
OuterEndcapPlanarDigiProcessor.ResolutionU = [0.007, 0.007, 0.007, 0.007, 0.007]
OuterEndcapPlanarDigiProcessor.ResolutionV = [0.09, 0.09, 0.09, 0.09, 0.09]
OuterEndcapPlanarDigiProcessor.SimTrackHitCollectionName = "OuterTrackerEndcapCollection"
OuterEndcapPlanarDigiProcessor.SimTrkHitRelCollection = "OuterTrackerEndcapHitsRelations"
OuterEndcapPlanarDigiProcessor.SubDetectorName = "OuterTrackers"
OuterEndcapPlanarDigiProcessor.TrackerHitCollectionName = "OTrackerEndcapHits"

TrackingDigiSequence = [
    VXDBarrelDigitiser,
    VXDEndcapDigitiser,
    InnerPlanarDigiProcessor,
    InnerEndcapPlanarDigiProcessor,
    OuterPlanarDigiProcessor,
    OuterEndcapPlanarDigiProcessor,
]
