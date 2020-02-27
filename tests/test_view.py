import blrequests.view as view
import testdata

def test_tabulate_empty_table():
    assert view.tabulate_table([]) == ""

def test_tabulate_isou_1row_table():
    isou_tabulated = view.tabulate_table(testdata.isou_1row_table)
    assert len(isou_tabulated.split("\n")) == 3 # three lines
    assert "ISOU" in isou_tabulated # has author's surname
    assert "author" in isou_tabulated # has keys as headers
