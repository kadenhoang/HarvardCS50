from working import convert

def test_valid():
    assert convert("9 AM to 9 PM") == "9:00 to 21:00"
