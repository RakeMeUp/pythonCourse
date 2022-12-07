from hamming import hamming_distance


def test_hamming_distance():
    assert hamming_distance("toned", "roses") == 3
    assert hamming_distance("tomb", "comb") == 1
    assert hamming_distance("fake", "poke") == 2
