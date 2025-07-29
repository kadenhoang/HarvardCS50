from seasons import check_birthday


def test_birthday():
    assert check_birthday("June 7,1995") == None
    assert check_birthday("1995-01-01") == ("1995","01","01")
    assert check_birthday("1995-1-1") == None


