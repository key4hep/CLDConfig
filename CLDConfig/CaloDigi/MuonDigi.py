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
from Configurables import DDSimpleMuonDigi
from Configurables import CollectionMerger
from Gaudi.Configuration import WARNING
from py_utils import toMarlinDict

input_collections = ["YokeBarrelCollection", "YokeEndcapCollection"]
output_collections = ["MuonYokeBarrelCollection", "MuonYokeEndcapCollection"]
output_relation = ["RelationMuonYokeBarrelHit", "RelationMuonYokeEndcapHit"]
names = ["Barrel", "Endcap"]

MyDDSimpleMuonDigiParameters = {
    "CalibrMUON": 70.1,
    "MaxHitEnergyMUON": 2.0,
    "MuonThreshold": 1e-06,
}

if reco_args.native:
    MuonDigiSequence = []
    for i in range(len(input_collections)):
        MyDDSimpleMuonDigi = DDSimpleMuonDigi(f"MyDDSimpleMuonDigi_{names[i]}",
                                              MUONCollection=[input_collections[i]],
                                              MUONOutputCollection=[output_collections[i]],
                                              RelationOutputCollection=[output_relation[i]],
                                              **MyDDSimpleMuonDigiParameters)
        MuonDigiSequence.append(MyDDSimpleMuonDigi)
    merger = CollectionMerger("MuonYokeMerger")
    merger.InputCollections = output_collections
    merger.OutputCollection = ["MUON"]

    relation_merger = CollectionMerger("MuonRelationMerger")
    relation_merger.InputCollections = output_relation
    relation_merger.OutputCollection = ["RelationMuonHit"]
    MuonDigiSequence += [merger, relation_merger]
else:
    from Configurables import MarlinProcessorWrapper
    MyDDSimpleMuonDigiParameters["MUONCollection"] = input_collections
    MyDDSimpleMuonDigiParameters["MUONCollections"] = ["MUON"]
    MyDDSimpleMuonDigiParameters["MUONOutputCollections"] = ["RelationMuonHit"]
    MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
    MyDDSimpleMuonDigi.OutputLevel = WARNING
    MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
    MyDDSimpleMuonDigi.Parameters = toMarlinDict(MyDDSimpleMuonDigiParameters)
    MuonDigiSequence = [MyDDSimpleMuonDigi]
