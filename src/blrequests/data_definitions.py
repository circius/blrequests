""" data definitions for blrequests
"""
from typing import NewType
from typing import Tuple

""" A BLTABLE is a [List-of BLROW]
"""

BlTable = NewType("BlTable", list)


""" A BLROW is a Dictionary with the following compulsory entries:
        'title' -> STRING
        'author' -> STRING
        'shelfmark' -> STRING
        'year' -> STRING
        'volume' -> STRING
        'notes' -> STRING
        'status' -> STRING
        'deliver to' -> STRING
        'date required' -> STRING
"""
BlRow = NewType("BlRow", dict)

Credentials = NewType("Credentials", Tuple[str, str])
