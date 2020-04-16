# -*- coding: utf-8 -*-
"""Encapsulates functions which handle credentials.

"""
from blrequests.data_definitions import Credentials
import subprocess
import configparser
import os.path

CONFIG_FILE = ".blrequestsrc"
CONFIG_FILE_EXISTS = os.path.exists(CONFIG_FILE)


def fetch_credentials() -> Credentials:
    """Produces a Credentials object based on the contents of the
CONFIG_FILE or, alternatively, interactively.

    """
    if CONFIG_FILE_EXISTS:
        return parse_config_file(CONFIG_FILE)
    else:
        return get_credentials_interactively()


def get_pass_output(parameter: str) -> str:
    """consumes a parameter for the GNU password manager PASS and
produces the corresponding output of that program.

    """
    return subprocess.run(
        ["pass", parameter], capture_output=True, text=True
    ).stdout.strip()


def parse_config_file(filepath: str) -> Credentials:
    """Produces a Credentials object based on the contents of a config
file.

    """
    config = configparser.ConfigParser()
    config.read(filepath)
    print(config)
    print([config["Authentication"][option] for option in config["Authentication"]])
    username, password, passeval = [
        config["Authentication"][option] for option in config["Authentication"]
    ]
    if passeval:
        password = get_pass_output(passeval)
    return (username, password)


def get_credentials_interactively() -> Credentials:
    """ Gets credentials for the bl interactively
"""
    return ("placeholder-user", "placeholder-pass")
