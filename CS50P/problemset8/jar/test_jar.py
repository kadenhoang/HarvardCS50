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
