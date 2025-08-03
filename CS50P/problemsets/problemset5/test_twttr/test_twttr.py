from twttr import shorten

def test_lowercase():
    assert shorten("David") == "Dvd"
    assert shorten("Codcacola") == "Cdccl"

def test_uppercase():
    assert shorten("dAvId") == "dvd"
    assert shorten("DAVID") == "DVD"

def test_digit():
    assert shorten("D4vid") == "D4vd"

def test_punctuation():
    assert shorten("D!#id") == "D!#d"



