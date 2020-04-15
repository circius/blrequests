import testdata
import os
from blrequests import authentication


def test_parses_config_file_with_password_correctly(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "blrequestsrc"
    p.write_text(testdata.blrequestsrc_password)
    print(authentication.parse_config_file(p))
    assert authentication.parse_config_file(p) == ("hello", "world")


def test_parses_config_file_with_passeval_correctly(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "blrequestsrc"
    p.write_text(testdata.blrequestsrc_passeval)
    # since we don't have some kind of mocked Pass, our test environment just blows out here.
    assert authentication.parse_config_file(p) == ("hello", "") 


def test_parses_config_file_with_passeval_and_password_correctly(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "blrequestsrc"
    p.write_text(testdata.blrequestsrc_passeval_and_password)
    # should blow out instead of using "world" as the password.
    assert authentication.parse_config_file(p) == ("hello", "")
