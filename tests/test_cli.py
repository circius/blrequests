import blrequests.cli
import subprocess

def test_cli():
    def test_bare_usage_stdout():
        result=subprocess.run(["blrequests"])
        expected="Hello World!"
        assert(result == expected)
