# -*- coding: utf-8 -*-
"""id-range-expand — expand compact id specs like ``B001-B005,R004`` into a list.

Handy whenever you let users type a terse selection of prefixed, zero-padded
ids — hosts, accounts, workers, shards — and you need the concrete list.

    from id_range_expand import expand

    expand("B001-B003,R004")     # ['B001', 'B002', 'B003', 'R004']
    expand("N7-N9")              # ['N7', 'N8', 'N9']   (width preserved from the low end)
    expand("A01-A03, A05")       # ['A01', 'A02', 'A03', 'A05']

Rules
-----
* Comma-separated parts; whitespace is ignored.
* A part ``PREFIX<lo>-[PREFIX]<hi>`` expands inclusively.
* Zero-padding width comes from the low bound (``B001`` -> width 3).
* A bare part (``R004``) passes through unchanged.
* Duplicates are removed while keeping first-seen order.
"""
from __future__ import annotations

import re

__all__ = ["expand", "parse_part"]

_RANGE = re.compile(r"^([A-Za-z]*)(\d+)\s*-\s*([A-Za-z]*)(\d+)$")


def parse_part(part: str) -> list[str]:
    part = part.strip()
    if not part:
        return []
    m = _RANGE.match(part)
    if not m:
        return [part]
    pre, lo_s, pre2, hi_s = m.groups()
    if pre2 and pre2 != pre:
        raise ValueError(f"prefix mismatch in range: {part!r}")
    lo, hi = int(lo_s), int(hi_s)
    if hi < lo:
        raise ValueError(f"range high < low: {part!r}")
    width = len(lo_s)
    return [f"{pre}{n:0{width}d}" for n in range(lo, hi + 1)]


def expand(spec: str) -> list[str]:
    """Expand a full spec string into a de-duplicated, ordered list of ids."""
    out: list[str] = []
    seen: set[str] = set()
    for part in spec.split(","):
        for item in parse_part(part):
            if item not in seen:
                seen.add(item)
                out.append(item)
    return out
