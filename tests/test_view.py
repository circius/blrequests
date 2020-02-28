import blrequests.view as view
import testdata


def test_tabulates_empty_table():
    assert view.tabulate_bltable([]) == ""


def test_tabulates_isou_1row_table():
    isou_tabulated = view.tabulate_bltable(testdata.isou_1row_table)
    assert len(isou_tabulated.split("\n")) == 3  # three lines
    assert "ISOU" in isou_tabulated  # has author's surname
    assert "author" in isou_tabulated  # has keys as headers


def test_tabulates_isou_1row_table_headerless():
    isou_tabulated = view.tabulate_bltable(testdata.isou_1row_table, headers=False)
    assert len(isou_tabulated.split("\n")) == 3  # three lines
    assert "ISOU" in isou_tabulated  # has author's surname
    assert "author" not in isou_tabulated  # has keys as headers
