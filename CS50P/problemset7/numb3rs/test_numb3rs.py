from numb3rs import validate

def test_outofrange():
    assert validate("256.1.1.1") == False
    assert validate("-1.2.3.4") == False

def test_inrange():
    assert validate("133.2.2.5") == True

def test_char():
    assert validate("salalala ding dong") == False

def test_specialsymbol():
    assert validate("+.##>.().>!!") == False
