import blrequests.app as app
from bs4 import BeautifulSoup
import testdata


def test_generates_bltable_from_soup():
    assert (
        app.table_generate_bltable(testdata.isou_table_soup) == testdata.isou_1row_table
    )


def test_gets_cells_from_rows():
    cells = app.row_get_cells(testdata.isou_row_soup)
    headers = app.HEADERS
    assert len(cells) == 9
    assert cells[0] == testdata.isou_row[headers[0]]
    assert cells[1] == testdata.isou_row[headers[1]]
    assert cells[2] == testdata.isou_row[headers[2]]
    assert cells[3] == testdata.isou_row[headers[3]]
    assert cells[4] == testdata.isou_row[headers[5]]
    assert cells[6] == testdata.isou_row[headers[6]]
    assert cells[7] == testdata.isou_row[headers[7]]
    assert cells[8] == testdata.isou_row[headers[8]]


def test_gets_BlRows_from_rows():
    cells = app.row_get_cells(testdata.isou_row_soup)
    assert app.row_generate_blrow(cells) == testdata.isou_row


def test_cleans_whitespace():
    assert app.cell_clean_whitespace("\t") == " "
    assert app.cell_clean_whitespace("\n") == " "
    assert app.cell_clean_whitespace("test\nthis") == "test this"
    assert app.cell_clean_whitespace("test\n\tthis") == "test this"
