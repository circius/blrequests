"""data for use in testing the various modules. should only be parsed
by pytest

"""
import os

THISDIR = os.path.dirname(__file__)

# this is a copy of a table from myrequests.bl.uk with one row
# note that
isou_table_file = os.path.join(THISDIR, "isou_table.html")
with open(isou_table_file, "r") as f:
    isou_table = f.read()

# this is a python dictionary, written by hand, of the contents of
# isou_table.
isou_row = {
    "title": "La création divine",
    "author": "ISOU, Isidore",
    "shelfmark": "X.512/2179",
    "year": "1972",
    "volume": "",
    "notes": "",
    "status": "Request submitted",
    "deliver to": "RARE BOOKS & MUSIC",
    "date required": "28 Feb 2020",
}

isou_1row_table = [isou_row]
