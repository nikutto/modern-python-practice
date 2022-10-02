def inc(x):
    return x + 1


def test_inc_2():
    assert inc(2) == 3


def test_inc_minus_1():
    assert inc(-1) == 0
