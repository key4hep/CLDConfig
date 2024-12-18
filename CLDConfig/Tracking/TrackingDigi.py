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
from Configurables import VTXdigitizer


VTXBarrelDigitizer = VTXdigitizer("VTXBarrelDigitizer",
                                  inputSimHits = "VertexBarrelCollection",
                                  outputDigiHits = "VTXTrackerBarrelHits",
                                  outputSimDigiAssociation = "VTXTrackerBarrelHitsRelations",
                                  detectorName = "Vertex",
                                  readoutName = "VertexBarrelCollection",
                                  xResolution = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
                                  yResolution = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
                                  tResolution = [1000,1000,1000,1000,1000,1000],
                                  forceHitsOntoSurface = False,
                                  OutputLevel = WARNING
                                  )

VTXEndcapDigitizer = VTXdigitizer("VTXEndcapDigitizer",
                                  inputSimHits = "VertexEndcapCollection",
                                  outputDigiHits = "VTXTrackerEndcapHits",
                                  outputSimDigiAssociation = "VTXTrackerEndcapHitsRelations",
                                  detectorName = "Vertex",
                                  readoutName = "VertexEndcapCollection",
                                  xResolution = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
                                  yResolution = [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
                                  tResolution = [1000,1000,1000,1000,1000,1000],
                                  forceHitsOntoSurface = False,
                                  OutputLevel = WARNING
                                  )

InnerTrackerBarrelDigitizer = VTXdigitizer("InnerTrackerBarrelDigitizer",
                                  inputSimHits = "InnerTrackerBarrelCollection",
                                  outputDigiHits = "InnerTrackerBarrelHits",
                                  outputSimDigiAssociation = "InnerTrackerBarrelHitsRelations",
                                  detectorName = "InnerTrackers",
                                  readoutName = "InnerTrackerBarrelCollection",
                                  xResolution = [0.007, 0.007, 0.007],
                                  yResolution = [0.09, 0.09, 0.09],
                                  tResolution = [1000,1000,1000],
                                  forceHitsOntoSurface = False,
                                  OutputLevel = WARNING
                                  )

InnerTrackerEndcapDigitizer = VTXdigitizer("InnerTrackerEndcapDigitizer",
                                  inputSimHits = "InnerTrackerEndcapCollection",
                                  outputDigiHits = "InnerTrackerEndcapHits",
                                  outputSimDigiAssociation = "InnerTrackerEndcapHitsRelations",
                                  detectorName = "InnerTrackers",
                                  readoutName = "InnerTrackerEndcapCollection",
                                  xResolution = [0.005, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007],
                                  yResolution = [0.005, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09],
                                  tResolution = [1000,1000,1000,1000,1000,1000,1000],
                                  forceHitsOntoSurface = False,
                                  OutputLevel = WARNING
                                  )

OuterTrackerBarrelDigitizer = VTXdigitizer("OuterTrackerBarrelDigitizer",
                                  inputSimHits = "OuterTrackerBarrelCollection",
                                  outputDigiHits = "OuterTrackerBarrelHits",
                                  outputSimDigiAssociation = "OuterTrackerBarrelHitsRelations",
                                  detectorName = "OuterTrackers",
                                  readoutName = "OuterTrackerBarrelCollection",
                                  xResolution = [0.007, 0.007, 0.007],
                                  yResolution = [0.09, 0.09, 0.09],
                                  tResolution = [1000,1000,1000],
                                  forceHitsOntoSurface = False,
                                  OutputLevel = WARNING
                                  )

OuterTrackerEndcapDigitizer = VTXdigitizer("OuterTrackerEndcapDigitizer",
                                  inputSimHits = "OuterTrackerEndcapCollection",
                                  outputDigiHits = "OuterTrackerEndcapHits",
                                  outputSimDigiAssociation = "OuterTrackerEndcapHitsRelations",
                                  detectorName = "OuterTrackers",
                                  readoutName = "OuterTrackerEndcapCollection",
                                  xResolution = [0.007, 0.007, 0.007, 0.007],
                                  yResolution = [0.09, 0.09, 0.09, 0.09],
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
