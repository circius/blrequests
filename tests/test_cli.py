import blrequests.cli
import subprocess

def test_bare_usage_stdout():
    result=subprocess.run(["blrequests"], capture_output=True)
    expected=b"Hello World!"
    assert(result.stdout.strip() == expected)
