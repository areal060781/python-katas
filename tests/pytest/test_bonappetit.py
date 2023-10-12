import pytest
from katas import bonappetit

testdata = [
    ([3, 10, 2, 9], 1, 12, 5),
    ([3, 10, 2, 9], 1, 7, "Bon Appetit")
]


@pytest.mark.parametrize("bill,k,b,expected", testdata)
def test_bon_appetit(bill, k, b, expected):
    assert bonappetit(bill, k, b) == expected
