from bank import value

def test_0():
    assert value("hello") == "$0"
    assert value("Hello what ?") == "$0"

def test_20():
    assert value("how are you") == "$20"
    assert value("hey") == "$20"

def test_100():
    assert value("what the hell?") == "$100"
    assert value("chickenman") == "$100"

def test_digit():
    assert value("134") == "$100"
    assert value("hello 5") == "$0"

def test_punctuation():
    assert value("!!!") == "$100"
    assert value("h!") == "$20"



