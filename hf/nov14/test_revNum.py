from revNum import reverseNumber


def test_reverseNumber():
    assert reverseNumber(123) == 321
    assert reverseNumber(465) == 564
    assert reverseNumber(7624) == 4267
    assert reverseNumber(996677) == 776699
