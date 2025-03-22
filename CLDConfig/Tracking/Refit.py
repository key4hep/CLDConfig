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

refit_args = {
    "EnergyLossOn": True,
    "InputRelationCollectionName": ["SiTrackRelations"],
    "InputTrackCollectionName": ["SiTracks"],
    "Max_Chi2_Incr": 1.79769e30,
    "MinClustersOnTrackAfterFit": 3,
    "MultipleScatteringOn": True,
    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
    "OutputTrackCollectionName": ["SiTracks_Refitted"],
    "ReferencePoint": -1,
    "SmoothOn": False,
    "extrapolateForward": True,
}

refit_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in refit_args.items()}
refit_args_marlin = {k: [str(v)] if isinstance(v, float) or isinstance(v, int) else v for k, v in refit_args_marlin.items()}


if args[0].native:
    from Configurables import RefitFinal

    Refit = RefitFinal(
        "RefitFinal",
        **refit_args,
        OutputLevel=WARNING,
    )
else:
    from Configurables import MarlinProcessorWrapper

    Refit = MarlinProcessorWrapper("Refit")
    Refit.OutputLevel = WARNING
    Refit.ProcessorType = "RefitFinal"
    Refit.Parameters = refit_args_marlin

RefitSequence = [
    Refit,
]
