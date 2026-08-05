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
from Gaudi.Configuration import INFO, DEBUG
from Configurables import MarlinProcessorWrapper

TrackLengthProcessor = MarlinProcessorWrapper("TrackLengthProcessor")
TrackLengthProcessor.OutputLevel = INFO
TrackLengthProcessor.ProcessorType = "TrackLengthProcessor"
TrackLengthProcessor.Parameters = {"ReconstructedParticleCollection": ["PandoraPFOs"]}

TOFEstimators0ps = MarlinProcessorWrapper("TOFEstimators0ps")
TOFEstimators0ps.OutputLevel = DEBUG
TOFEstimators0ps.ProcessorType = "TOFEstimators"
TOFEstimators0ps.Parameters = {
    "ExtrapolateToEcal": ["true"],
    "MaxEcalLayer": ["10"],
    "ReconstructedParticleCollection": ["PandoraPFOs"],
    "TimeResolution": ["0"],
    "TofMethod": ["closest"],
    "Verbosity": ["DEBUG9"],
}

TOFSequence = [
    TrackLengthProcessor,
    TOFEstimators0ps,
]
