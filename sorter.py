from enum import Enum


class Stack(Enum):
    STANDARD = "STANDARD"
    SPECIAL  = "SPECIAL"
    REJECTED = "REJECTED"


def _validate(width: int, height: int, length: int, mass: float) -> None:
    if not all(isinstance(d, int) for d in (width, height, length)):
        raise TypeError("width, height, and length must be integers (cm)")
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be a number (kg)")
    # zero width is allowed (e.g. a flat letter)
    if width < 0:
        raise ValueError("width must be 0 or greater")
    if height <= 0:
        raise ValueError("height must be greater than 0")
    if length <= 0:
        raise ValueError("length must be greater than 0")
    if mass <= 0:
        raise ValueError("mass must be greater than 0")


def _is_bulky(width: int, height: int, length: int) -> bool:
    """
    Args:
        width  (int): cm
        height (int): cm
        length (int): cm
    """
    # treat zero width as 1 cm so large flat packages are still considered bulky
    effective_width = width if width > 0 else 1
    volume = effective_width * height * length
    return volume >= 1_000_000 or any(d >= 150 for d in (width, height, length))


def _is_heavy(mass: float) -> bool:
    """
    Args:
        mass (float): kg
    """
    return mass >= 20


def _is_rejected(width: int, height: int, length: int, mass: float) -> bool:
    return _is_bulky(width, height, length) and _is_heavy(mass)


def _is_special(width: int, height: int, length: int, mass: float) -> bool:
    return _is_bulky(width, height, length) or _is_heavy(mass)


def sort(width: int, height: int, length: int, mass: float) -> Stack:
    """
    Dispatch a package to the correct stack.

    Args:
        width  (int):   cm
        height (int):   cm
        length (int):   cm
        mass   (float): kg

    Returns:
        Stack: Stack.STANDARD, Stack.SPECIAL, or Stack.REJECTED
    """
    _validate(width, height, length, mass)

    if _is_rejected(width, height, length, mass):
        return Stack.REJECTED
    if _is_special(width, height, length, mass):
        return Stack.SPECIAL
    return Stack.STANDARD
