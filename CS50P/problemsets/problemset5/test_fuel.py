import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    with pytest.raises(ValueError):
        convert("5/4")
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"

