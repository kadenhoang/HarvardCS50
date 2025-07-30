from jar import Jar

def test_withdraw():
    jar = Jar()
    assert jar.withdraw(-1) == ValueError
    assert jar.withdraw(1) 
