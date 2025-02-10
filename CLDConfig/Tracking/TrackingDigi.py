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
from Configurables import VTXdigitizerDetailed

VTXBarrelDigitizer = VTXdigitizerDetailed("VTXBarrelDigitizer",
                                          inputSimHits = "VertexBarrelCollection",
                                          outputDigiHits = "VTXTrackerBarrelHits",
                                          outputSimDigiAssociation = "VTXTrackerBarrelHitsRelations",
                                          detectorName = "VertexBarrel",
                                          readoutName = "VertexBarrelCollection",
                                          LocalNormalVectorDir = "x",
                                          tResolution = [1000,1000,1000,1000,1000,1000],
                                          forceHitsOntoSurface = False,
                                          OutputLevel = WARNING
                                          )

VTXEndcapDigitizer = VTXdigitizerDetailed("VTXEndcapDigitizer",
                                          inputSimHits = "VertexEndcapCollection",
                                          outputDigiHits = "VTXTrackerEndcapHits",
                                          outputSimDigiAssociation = "VTXTrackerEndcapHitsRelations",
                                          detectorName = "VertexEndcap",
                                          readoutName = "VertexEndcapCollection",
                                          LocalNormalVectorDir = "y",
                                          tResolution = [1000,1000,1000,1000,1000,1000],
                                          forceHitsOntoSurface = False,
                                          OutputLevel = WARNING
                                          )

InnerTrackerBarrelDigitizer = VTXdigitizerDetailed("InnerTrackerBarrelDigitizer",
                                                   inputSimHits = "InnerTrackerBarrelCollection",
                                                   outputDigiHits = "InnerTrackerBarrelHits",
                                                   outputSimDigiAssociation = "InnerTrackerBarrelHitsRelations",
                                                   detectorName = "InnerTrackerBarrel",
                                                   readoutName = "InnerTrackerBarrelCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [1000,1000,1000],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING
                                                   )

InnerTrackerEndcapDigitizer = VTXdigitizerDetailed("InnerTrackerEndcapDigitizer",
                                                   inputSimHits = "InnerTrackerEndcapCollection",
                                                   outputDigiHits = "InnerTrackerEndcapHits",
                                                   outputSimDigiAssociation = "InnerTrackerEndcapHitsRelations",
                                                   detectorName = "InnerTrackerEndcap",
                                                   readoutName = "InnerTrackerEndcapCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [1000,1000,1000,1000,1000,1000,1000],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING
                                                   )

OuterTrackerBarrelDigitizer = VTXdigitizerDetailed("OuterTrackerBarrelDigitizer",
                                                   inputSimHits = "OuterTrackerBarrelCollection",
                                                   outputDigiHits = "OuterTrackerBarrelHits",
                                                   outputSimDigiAssociation = "OuterTrackerBarrelHitsRelations",
                                                   detectorName = "OuterTrackerBarrel",
                                                   readoutName = "OuterTrackerBarrelCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [1000,1000,1000],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING
                                                   )

OuterTrackerEndcapDigitizer = VTXdigitizerDetailed("OuterTrackerEndcapDigitizer",
                                                   inputSimHits = "OuterTrackerEndcapCollection",
                                                   outputDigiHits = "OuterTrackerEndcapHits",
                                                   outputSimDigiAssociation = "OuterTrackerEndcapHitsRelations",
                                                   detectorName = "OuterTrackerEndcap",
                                                   readoutName = "OuterTrackerEndcapCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [1000,1000,1000,1000],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING
                                                   )

TrackingDigiSequence = [
    VTXBarrelDigitizer,
    VTXEndcapDigitizer,
    InnerTrackerBarrelDigitizer,
    InnerTrackerEndcapDigitizer,
    OuterTrackerBarrelDigitizer,
    OuterTrackerEndcapDigitizer
]
