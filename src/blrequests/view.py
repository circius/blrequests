"""encapsulates functions which generate representations of
bltables.

"""
from tabulate import tabulate
from typing import NewType

""" A BLTABLE is a [List-of BLROW]
"""

BlTable = NewType('BlTable', list)


""" A BLROW is a Dictionary with the following compulsory entries:
        'title' -> STRING
        'author' -> STRING
        'shelfmark' -> STRING
        'year' -> STRING
        'status' -> STRING
        'deliver_to' -> STRING
        'date_required' -> STRING
"""
BlRow = NewType('BlRow', dict)

