from twttr import shorten

def test_lowercase():
    assert shorten("David") == "Dvd"

def test_uppercase():
    assert shorten("dAvId") == "dvd"

def test_numbers():
    assert shorten("d4v1d") == "dvd"

def test_punctualtion():
    assert shortenn("d!v!d") == "dvd"

