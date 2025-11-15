import pytest
from id_range_expand import expand, parse_part

def test_basic():
    assert expand("B001-B003") == ["B001", "B002", "B003"]

def test_mixed_and_bare():
    assert expand("B001-B002,R004") == ["B001", "B002", "R004"]

def test_width():
    assert expand("N7-N9") == ["N7", "N8", "N9"]
    assert expand("A01-A03") == ["A01", "A02", "A03"]

def test_dedup_order():
    assert expand("A05, A01-A03, A05") == ["A05", "A01", "A02", "A03"]

def test_prefix_mismatch():
    with pytest.raises(ValueError):
        parse_part("B001-C003")

def test_reversed():
    with pytest.raises(ValueError):
        parse_part("B005-B001")
