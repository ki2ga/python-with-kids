from chapter1 import add1, repeat5, first_and_last, split

def test_1():
    assert add1(2) == 3

def test_2():
    assert add1(10) == 11

def test_3():
    assert repeat5(3) == '33333'

def test_4():
    assert first_and_last([1,2,3,4,5]) == '15'

def test_5():
    assert split([1,2,3,4,5,6,7,8], 5) == ([1,2,3,4], [5,6,7,8])

def test_6():
    assert split([1,24,13,2,22,2,0], 15) == ([1,13,2,2,0], [24,22])