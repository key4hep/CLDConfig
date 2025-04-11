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
from Configurables import k4MLJetTagger
import yaml

if reco_args.enableMLJetTagger:
    # check if jet clustering is also enabled (prerequisite for jet flavor tagging)
    if not reco_args.enableLCFIJet:
        raise ValueError("MLJetTagger requires LCFIPlus jet clustering to be enabled. Please add --enableLCFIJet to the command or disable --enableMLJetTagger.")
    
    # load yaml config about model types
    with open("models_MLJetTagger.yaml", "r") as file:
        model_config = yaml.safe_load(file)
    
    # check if the model type is valid
    if reco_args.MLJetTaggerModel not in model_config:
        raise ValueError(f"Invalid model type '{reco_args.MLJetTaggerModel}'. Valid options are: {', '.join(model_config.keys())}.")

    # load the model configuration
    onnx_model = model_config[reco_args.MLJetTaggerModel]["onnx_model"]
    json_onnx_config = model_config[reco_args.MLJetTaggerModel]["json_onnx_config"]
    flavor_collection_names = model_config[reco_args.MLJetTaggerModel]["flavor_collection_names"]

    # print out the model configuration
    print(f"Using MLJetTagger model: \t\t {reco_args.MLJetTaggerModel}\n",
          f"The model uses the architecture: \t {model_config[reco_args.MLJetTaggerModel]['model']}\n",
          f"was trained on the kinematics: \t {model_config[reco_args.MLJetTaggerModel]['kinematics']}\n",
          f"and the detector version: \t\t {model_config[reco_args.MLJetTaggerModel]['detector']}\n",
          f"at a center-of-mass energy of: \t {model_config[reco_args.MLJetTaggerModel]['ecm']} GeV\n",
          f"Comment: \t\t\t\t {model_config[reco_args.MLJetTaggerModel]['comment']}\n",
          f"Appending collections to the event: \t {', '.join(flavor_collection_names)}\n",)

    # create the MLJetTagger algorithm

    k4MLJetTagger = JetTagger("JetTagger",
                        model_path=onnx_model,
                        json_path=json_onnx_config,
                        flavor_collection_names = flavor_collection_names, # to make sure the order and nameing is correct
                        InputJets=["RefinedVertexJets"],
                        InputPrimaryVertices=["PrimaryVertices"],
                        OutputIDCollections=flavor_collection_names,
                        )

    # append sequence to the algorithm list
    MLJetTaggerSequence = [
        k4MLJetTagger,
    ]
