#
# Copyright (c) 2014-2023 Key4hep-Project.
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
import os
import subprocess
from decorator import decorator
import pytest

@decorator
def _CLDConfig(test_fun):
    os.chdir("CLDConfig")
    test_fun()
    os.chdir("..")

detectorModel = os.path.join(os.environ["K4GEO"], "FCCee/CLD/compact/FCCee_o1_v04/FCCee_o1_v04.xml")

@_CLDConfig
@pytest.mark.dependency()
def test_ddsim_lcio():
    command = "ddsim -S cld_steer.py -N 3 --inputFile ../test/yyxyev_000.stdhep --outputFile test.slcio".split()
    command.extend(["--compactFile", detectorModel])
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout

@_CLDConfig
@pytest.mark.dependency()
def test_ddsim_edm4hep():
    command = "ddsim -S cld_steer.py -N 3 --inputFile ../test/yyxyev_000.stdhep --outputFile test.edm4hep.root".split()
    command.extend(["--compactFile", detectorModel])
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout

@_CLDConfig
@pytest.mark.dependency(depends=["test_ddsim_lcio"])
def test_lcio_input():
    command = "k4run --inputFiles=test.slcio --outputBasename=rec_test_lcio CLDReconstruction.py".split()
    command.extend(["--GeoSvc.detectors", detectorModel])
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout

@_CLDConfig
@pytest.mark.dependency(depends=["test_ddsim_edm4hep"])
def test_edm4hep_input():
    command = "k4run --inputFiles=test.edm4hep.root --outputBasename=rec_test_edm4hep CLDReconstruction.py".split()
    command.extend(["--GeoSvc.detectors", detectorModel])
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout
