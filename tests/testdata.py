"""data for use in testing the various modules. should only be parsed
by pytest

"""
import os
from bs4 import BeautifulSoup

THISDIR = os.path.dirname(__file__)

# this is a copy of a table from myrequests.bl.uk with one row
# note that
isou_table_file = os.path.join(THISDIR, "isou_table.html")
with open(isou_table_file, "r") as f:
    isou_table = f.read()

# this is a copy of a row from isou_table_file
isou_row_file = os.path.join(THISDIR, "isou_row.html")
with open(isou_row_file, "r") as f:
    isou_row = f.read()


isou_table_soup = BeautifulSoup(isou_table, "html.parser")
isou_row_soup = BeautifulSoup(isou_row, "html.parser")

# this is a python dictionary whose values correspond exactly to the
# contents of isou_table, with \n, \r and \xa0 stripped. This is what
# we test against for now.
isou_row = {
    "title": "La création divine, la transformati -on récente de l'Ég...",
    "author": "ISOU, Isidore,",
    "shelfmark": "X.512/2179.",
    "year": "1972",
    "volume": "",
    "notes": "",
    "status": "Request submitted",
    "deliver to": "RARE BOOKS & MUSIC",
    "date required": "28 Feb 2020",
}

isou_1row_table = [isou_row]
