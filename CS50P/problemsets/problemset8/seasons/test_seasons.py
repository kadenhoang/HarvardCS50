from seasons import check_birthday


def test_valid_birthday():
    assert check_birthday("1995-01-01") == ("1995","01","01")

def test_invalid_birthday():
    assert check_birthday("June 7,1995") == None

def test_incomplete():
    assert check_birthday("1995-1-1") == None


