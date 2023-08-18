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
    res = subprocess.run("k4run --inputFile=../test.slcio --outputBasename=rec_test CLDReconstruction.py".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert res.returncode == 0, res.stdout[-(30*80):]