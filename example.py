"""Run: python example.py"""
from id_range_expand import expand
for spec in ["B001-B003,R004", "N7-N9", "A01-A03, A05, A05"]:
    print(f"{spec:22} -> {expand(spec)}")
