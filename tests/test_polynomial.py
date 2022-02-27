from polynomials import Polynomial


def test_print():

    p = Polynomial((2,1,0,3))

    assert str(p) == "3x^3 + x + 2"

#simply input pytest in the command line can do the test

#pytest -x test will stop when it find the first failed test 