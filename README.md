# Package Sorter

A Python module for Smarter Technology's robotic automation factory that dispatches packages to the correct stack based on their dimensions and mass.

## Rules

A package is **bulky** if:
- Its volume (width × height × length) is >= 1,000,000 cm³, or
- Any single dimension is >= 150 cm

A package is **heavy** if:
- Its mass is >= 20 kg

| Condition | Stack |
|---|---|
| Neither bulky nor heavy | `STANDARD` |
| Bulky or heavy (but not both) | `SPECIAL` |
| Both bulky and heavy | `REJECTED` |

## Usage

```python
from sorter import sort, Stack

result = sort(100, 100, 100, 25)  # REJECTED
result = sort(200, 10, 10, 1)     # SPECIAL
result = sort(10, 10, 10, 1)      # STANDARD
```

`sort()` returns a `Stack` enum value: `Stack.STANDARD`, `Stack.SPECIAL`, or `Stack.REJECTED`.

## Input

| Parameter | Type | Unit | Constraints |
|---|---|---|---|
| `width` | `int` | cm | >= 0 (0 is valid for flat letters) |
| `height` | `int` | cm | > 0 |
| `length` | `int` | cm | > 0 |
| `mass` | `float` | kg | > 0 |

Raises `TypeError` for wrong types and `ValueError` for invalid values.

## Running Tests

```bash
python test_sorter.py

# or with pytest
pytest test_sorter.py -v
```
