# id-range-expand

Expand compact id specs like `B001-B005,R004` into a concrete list — for prefixed, zero-padded ids (hosts, accounts, workers, shards). Zero dependencies.

## Usage

```python
from id_range_expand import expand

expand("B001-B003,R004")     # ['B001', 'B002', 'B003', 'R004']
expand("N7-N9")              # ['N7', 'N8', 'N9']
expand("A01-A03, A05")       # ['A01', 'A02', 'A03', 'A05']
```

- Comma-separated parts; whitespace ignored.
- `PREFIX<lo>-[PREFIX]<hi>` expands inclusively; padding width from the low bound.
- Bare parts pass through; duplicates removed (first-seen order kept).

## License
MIT — see [LICENSE](LICENSE).
