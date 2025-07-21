from working import convert

def test_valid():
    assert convert("9:00 AM to 9:00 PM") == "9 AM to 9 PM"
