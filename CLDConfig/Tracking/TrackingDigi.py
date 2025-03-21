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

vxd_barrel_digitiser_args = {
    "IsStrip": False,
    "ResolutionU": [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
    "ResolutionV": [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
    "SimTrackerHitCollectionName": ["VertexBarrelCollection"],
    "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
    "SubDetectorName": ["Vertex"],
    "TrackerHitCollectionName": ["VXDTrackerHits"],
    "OutputLevel": WARNING,
}

vxd_endcap_digitiser_args = {
    "IsStrip": False,
    "ResolutionU": [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
    "ResolutionV": [0.003, 0.003, 0.003, 0.003, 0.003, 0.003],
    "SimTrackerHitCollectionName": ["VertexEndcapCollection"],
    "SimTrkHitRelCollection": ["VXDEndcapTrackerHitRelations"],
    "SubDetectorName": ["Vertex"],
    "TrackerHitCollectionName": ["VXDEndcapTrackerHits"],
    "OutputLevel": WARNING,
}

inner_planar_digi_processor_args = {
    "IsStrip": False,
    "ResolutionU": [0.007],
    "ResolutionV": [0.09],
    "SimTrackerHitCollectionName": ["InnerTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["InnerTrackerBarrelHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TrackerHitCollectionName": ["ITrackerHits"],
    "OutputLevel": WARNING,
}

inner_endcap_planar_digi_processor_args = {
    "IsStrip": False,
    "ResolutionU": [0.005, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007],
    "ResolutionV": [0.005, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09],
    "SimTrackerHitCollectionName": ["InnerTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["InnerTrackerEndcapHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TrackerHitCollectionName": ["ITrackerEndcapHits"],
    "OutputLevel": WARNING,
}

outer_planar_digi_processor_args = {
    "IsStrip": False,
    "ResolutionU": [0.007, 0.007, 0.007],
    "ResolutionV": [0.09, 0.09, 0.09],
    "SimTrackerHitCollectionName": ["OuterTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["OuterTrackerBarrelHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TrackerHitCollectionName": ["OTrackerHits"],
    "OutputLevel": WARNING,
}

outer_endcap_planar_digi_processor_args = {
    "IsStrip": False,
    "ResolutionU": [0.007, 0.007, 0.007, 0.007, 0.007],
    "ResolutionV": [0.09, 0.09, 0.09, 0.09, 0.09],
    "SimTrackerHitCollectionName": ["OuterTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["OuterTrackerEndcapHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TrackerHitCollectionName": ["OTrackerEndcapHits"],
    "OutputLevel": WARNING,
}


vxd_barrel_digitiser_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in vxd_barrel_digitiser_args.items()}
vxd_barrel_digitiser_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in vxd_barrel_digitiser_args_marlin.items()}
vxd_endcap_digitiser_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in vxd_endcap_digitiser_args.items()}
vxd_endcap_digitiser_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in vxd_endcap_digitiser_args_marlin.items()}
inner_planar_digi_processor_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in inner_planar_digi_processor_args.items()}
inner_planar_digi_processor_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in inner_planar_digi_processor_args_marlin.items()}
inner_endcap_planar_digi_processor_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in inner_endcap_planar_digi_processor_args.items()}
inner_endcap_planar_digi_processor_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in inner_endcap_planar_digi_processor_args_marlin.items()}
outer_planar_digi_processor_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in outer_planar_digi_processor_args.items()}
outer_planar_digi_processor_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in outer_planar_digi_processor_args_marlin.items()}
outer_endcap_planar_digi_processor_args_marlin = {k: [str(v).lower()] if isinstance(v, bool) else v for k, v in outer_endcap_planar_digi_processor_args.items()}
outer_endcap_planar_digi_processor_args_marlin = {k: [str(elem) for elem in v] if isinstance(v, list) else v for k, v in outer_endcap_planar_digi_processor_args_marlin.items()}


if args[0].native:
    from Configurables import DDPlanarDigi

    VXDBarrelDigitiser = DDPlanarDigi(
        "VXDBarrelDigitiser",
        **vxd_barrel_digitiser_args
    )
    VXDEndcapDigitiser = DDPlanarDigi(
        "VXDEndcapDigitiser",
        **vxd_endcap_digitiser_args
    )
    InnerPlanarDigiProcessor = DDPlanarDigi(
        "InnerPlanarDigiProcessor",
        **inner_planar_digi_processor_args
    )
    InnerEndcapPlanarDigiProcessor = DDPlanarDigi(
        "InnerEndcapPlanarDigiProcessor",
        **inner_endcap_planar_digi_processor_args
    )
    OuterPlanarDigiProcessor = DDPlanarDigi(
        "OuterPlanarDigiProcessor",
        **outer_planar_digi_processor_args
    )

    OuterEndcapPlanarDigiProcessor = DDPlanarDigi(
        "OuterEndcapPlanarDigiProcessor",
        **outer_endcap_planar_digi_processor_args
    )

else:
    from Configurables import MarlinProcessorWrapper

    VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
    VXDBarrelDigitiser.OutputLevel = WARNING
    VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
    VXDBarrelDigitiser.Parameters = vxd_barrel_digitiser_args_marlin

    VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
    VXDEndcapDigitiser.OutputLevel = WARNING
    VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
    VXDEndcapDigitiser.Parameters = vxd_endcap_digitiser_args_marlin

    InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
    InnerPlanarDigiProcessor.OutputLevel = WARNING
    InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
    InnerPlanarDigiProcessor.Parameters = inner_planar_digi_processor_args_marlin

    InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
        "InnerEndcapPlanarDigiProcessor"
    )
    InnerEndcapPlanarDigiProcessor.OutputLevel = WARNING
    InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
    InnerEndcapPlanarDigiProcessor.Parameters = inner_endcap_planar_digi_processor_args_marlin

    OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
    OuterPlanarDigiProcessor.OutputLevel = WARNING
    OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
    OuterPlanarDigiProcessor.Parameters = outer_planar_digi_processor_args_marlin

    OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
        "OuterEndcapPlanarDigiProcessor"
    )
    OuterEndcapPlanarDigiProcessor.OutputLevel = WARNING
    OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
    OuterEndcapPlanarDigiProcessor.Parameters = outer_endcap_planar_digi_processor_args_marlin

TrackingDigiSequence = [
    VXDBarrelDigitiser,
    VXDEndcapDigitiser,
    InnerPlanarDigiProcessor,
    InnerEndcapPlanarDigiProcessor,
    OuterPlanarDigiProcessor,
    OuterEndcapPlanarDigiProcessor,
]
