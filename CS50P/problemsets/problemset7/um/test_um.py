from um import count

def test_string():
    assert count("yummy") == 0
    assert count("yumyumyum") == 0

def testum():
    assert count("hello, um") == 1
    assert count("hello, um ,world,um") == 2
