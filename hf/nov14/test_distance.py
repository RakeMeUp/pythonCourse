from distance import distance


def test_distance():
    assert distance((1, 3), (1, 3)) == 0.0
    assert distance((1, 2), (6, 5)) == 5.830951894845301
    assert distance((1, 2), (1, 3)) == 1.0
