from verem import Verem


def test_Verem_betesz():
    v = Verem()
    v.betesz(1)
    assert v.top() == 1


def test_Verem_meret():
    v = Verem()
    v.betesz(1)
    assert v.meret() == 1


def test_Verem_kivesz():
    v = Verem()
    v.betesz(1)
    v.kivesz()
    assert v.meret() == 0


def test_Verem_ures():
    v = Verem()
    assert v.ures() == True
