"""encapsulates functions which generate representations of
bltables.

"""
from tabulate import tabulate
from typing import NewType

""" A BLTABLE is a [List-of BLROW]
"""

BlTable = NewType("BlTable", list)


""" A BLROW is a Dictionary with the following compulsory entries:
        'title' -> STRING
        'author' -> STRING
        'shelfmark' -> STRING
        'year' -> STRING
        'status' -> STRING
        'deliver_to' -> STRING
        'date_required' -> STRING
"""
BlRow = NewType("BlRow", dict)


def tabulate_table(
    table: BlTable, headers: bool = True, table_format: str = "simple"
) -> str:
    """Consumes a BlTable and produces a String representing it in some
TABLE_FORMAT, ready to be printed to a console. If HEADERS is false,
no header-row will be generated.

Note that TABLE_FORMAT is simply passed to the identically-named
variable in tabulate, so we can use any output format recognised by
tabulate.

    """
    if not headers:
        return tabulate(table, tablefmt=table_format)
    else:
        return tabulate(table, headers="keys", tablefmt=table_format)
