from jar import Jar

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_invalid_withdraw():
    jar = Jar()
    jar.deposit(5)
    try:
        jar.withdraw(10)
    except ValueError:
        assert True
    else:
        assert False

def test_invalid_deposit():
    jar = Jar()
    try:
        jar.deposit(100)
    except ValueError:
        assert True
    else:
        assert False

