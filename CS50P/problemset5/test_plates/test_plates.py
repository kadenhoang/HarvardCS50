from plates import is_valid

def test_len():
    assert is_valid("2") == False
    assert is_valid("AA222") == True

def test_2firstelements():
    assert is_valid("AA123") == True
    assert is_valid("123AA") == False

def test_firstdigit0():
    assert is_valid("AA0") == True
    assert is_valid("AA123") == True

def test_afterdigit():
    assert is_valid("AA1A") == True
    assert is_valid("AAA111") == True
