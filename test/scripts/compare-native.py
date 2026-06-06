#!/usr/bin/env python
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



# A simple script to compare collections between the native and wrapped Marlin reconstruction output
import argparse
from podio.reading import get_reader

parser = argparse.ArgumentParser(description="Compare hits from Gaudi and Marlin")
parser.add_argument(
    "--native-file", default="output_native_REC.edm4hep.root", help="Gaudi native output file"
)
parser.add_argument(
    "--wrapped-file", default="output_REC.edm4hep.root", help="Wrapped output file"
)

args = parser.parse_args()

reader_native = get_reader(args.native_file)
reader_wrapped = get_reader(args.wrapped_file)

events_native = reader_native.get("events")
events_wrapped = reader_wrapped.get("events")

EXPECTED_MISSING = set([])
EXPECTED_EXTRA = set([])

for i, frame_native in enumerate(events_native):
    frame_wrapped = events_wrapped[i]
    collections_native = set(frame_native.getAvailableCollections())
    collections_wrapped = set(frame_wrapped.getAvailableCollections())
    extra = collections_native - collections_wrapped
    missing = collections_wrapped - collections_native
    common = collections_native & collections_wrapped
    if missing:
        print(f"Event {i}: Missing collections in native: {missing}")
        if not missing.issubset(EXPECTED_MISSING):
            print("Unexpected missing collections found!")
    if extra:
        print(f"Event {i}: Extra collections in native: {extra}")
        if not extra.issubset(EXPECTED_EXTRA):
            print("Unexpected extra collections found!")
    are_sizes_different = False
    for coll in common:
        data_native = frame_native.get(coll)
        data_wrapped = frame_wrapped.get(coll)
        if len(data_native) != len(data_wrapped):
            print(f"Event {i}: Collection '{coll}' has different lengths: "
                  f"{len(data_native)} in native, {len(data_wrapped)} in wrapped.")
            are_sizes_different = True
    # if missing or extra:
    if are_sizes_different:
        raise ValueError("Collections do not match between Gaudi and wrapped Marlin output.")
