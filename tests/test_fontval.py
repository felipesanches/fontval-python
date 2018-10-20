from __future__ import absolute_import, unicode_literals
import pytest
import subprocess
import fontval

# FIXME: Fix these and implement more checks here.

#def test_run_checks():
#    p = fontval.run_checks("-file", os.path.join(["data","test","mada", "Mada-Regular.ttf"]))
#    assert p.returncode == 1
#    assert len(p.args) == 3
#    assert p.args[0].endswith("FontValidator.exe")
#    assert p.stdout == None
#    assert p.stderr == None

def test_check_error():
    with pytest.raises(subprocess.CalledProcessError):
        fontval.run_checks("--foo", "bar", check=True)


#def test_capture_output():
#    p = fontval.run_checks(capture_output=True)
#    assert len(p.stdout) == 0
#    stderr = p.stderr.decode()
#    assert stderr.startswith("Usage: ")
