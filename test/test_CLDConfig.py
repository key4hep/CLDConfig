import os
import subprocess
from decorator import decorator

@decorator
def _CLDConfig(test_fun):
    os.chdir("CLDConfig")
    test_fun()
    os.chdir("..")


@_CLDConfig
def test_lcio_edm4hep():
    command = "k4run --inputFiles=../test.slcio --outputBasename=rec_test CLDReconstruction.py".split()
    detectorModel = os.path.join(os.environ["K4GEO"], "FCCee/CLD/compact/FCCee_o1_v04/FCCee_o1_v04.xml")
    command.extend(["--GeoSvc.detectors", detectorModel])
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout
