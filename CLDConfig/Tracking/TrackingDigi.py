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
                                          outputDigiHits = "VXDTrackerHitsEDM4HEP",
                                          outputSimDigiAssociation = "VXDTrackerHitRelationsEDM4HEP",
                                          detectorName = "VertexBarrel",
                                          readoutName = "VertexBarrelCollection",
                                          LocalNormalVectorDir = "x",
                                          tResolution = [0.,0.,0.,0.,0.,0.],
                                          forceHitsOntoSurface = False,
                                          OutputLevel = WARNING,
                                          DebugHistos = True,
                                          DebugFileName = "Debug_VTXBarrelDigitizer.root"
                                          )

VTXEndcapDigitizer = VTXdigitizerDetailed("VTXEndcapDigitizer",
                                          inputSimHits = "VertexEndcapCollection",
                                          outputDigiHits = "VXDEndcapTrackerHitsEDM4HEP",
                                          outputSimDigiAssociation = "VXDEndcapTrackerHitRelationsEDM4HEP",
                                          detectorName = "VertexEndcap",
                                          readoutName = "VertexEndcapCollection",
                                          LocalNormalVectorDir = "y",
                                          tResolution = [0.,0.,0.,0.,0.,0.],
                                          forceHitsOntoSurface = False,
                                          OutputLevel = WARNING,
                                          DebugHistos = True,
                                          DebugFileName = "Debug_VTXEndcapDigitizer.root"
                                          )

InnerTrackerBarrelDigitizer = VTXdigitizerDetailed("InnerTrackerBarrelDigitizer",
                                                   inputSimHits = "InnerTrackerBarrelCollection",
                                                   outputDigiHits = "ITrackerHitsEDM4HEP",
                                                   outputSimDigiAssociation = "InnerTrackerBarrelHitsRelationsEDM4HEP",
                                                   detectorName = "InnerTrackerBarrel",
                                                   readoutName = "InnerTrackerBarrelCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [0.,0.,0.],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING,
                                                   DebugHistos = True,
                                                   DebugFileName = "Debug_InnerTrackerBarrelDigitizer.root"
                                                   )

InnerTrackerEndcapDigitizer = VTXdigitizerDetailed("InnerTrackerEndcapDigitizer",
                                                   inputSimHits = "InnerTrackerEndcapCollection",
                                                   outputDigiHits = "ITrackerEndcapHitsEDM4HEP",
                                                   outputSimDigiAssociation = "InnerTrackerEndcapHitsRelationsEDM4HEP",
                                                   detectorName = "InnerTrackerEndcap",
                                                   readoutName = "InnerTrackerEndcapCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [0.,0.,0.,0.,0.,0.,0.],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING,
                                                   DebugHistos = True,
                                                   DebugFileName = "Debug_InnerTrackerEndcapDigitizer.root"
                                                   )

OuterTrackerBarrelDigitizer = VTXdigitizerDetailed("OuterTrackerBarrelDigitizer",
                                                   inputSimHits = "OuterTrackerBarrelCollection",
                                                   outputDigiHits = "OTrackerHitsEDM4HEP",
                                                   outputSimDigiAssociation = "OuterTrackerBarrelHitsRelationsEDM4HEP",
                                                   detectorName = "OuterTrackerBarrel",
                                                   readoutName = "OuterTrackerBarrelCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [0.,0.,0.],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING,
                                                   DebugHistos = True,
                                                   DebugFileName = "Debug_OuterTrackerBarrelDigitizer.root"
                                                   )

OuterTrackerEndcapDigitizer = VTXdigitizerDetailed("OuterTrackerEndcapDigitizer",
                                                   inputSimHits = "OuterTrackerEndcapCollection",
                                                   outputDigiHits = "OTrackerEndcapHitsEDM4HEP",
                                                   outputSimDigiAssociation = "OuterTrackerEndcapHitsRelationsEDM4HEP",
                                                   detectorName = "OuterTrackerEndcap",
                                                   readoutName = "OuterTrackerEndcapCollection",
                                                   LocalNormalVectorDir = "z",
                                                   tResolution = [0.,0.,0.,0.],
                                                   forceHitsOntoSurface = False,
                                                   OutputLevel = WARNING,
                                                   DebugHistos = True,
                                                   DebugFileName = "Debug_OuterTrackerEndcapDigitizer.root"
                                                   )

TrackingDigiSequence = [
    VTXBarrelDigitizer,
    VTXEndcapDigitizer,
    InnerTrackerBarrelDigitizer,
    InnerTrackerEndcapDigitizer,
    OuterTrackerBarrelDigitizer,
    OuterTrackerEndcapDigitizer
]
