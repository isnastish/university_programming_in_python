import math


def compute_expression(x: float) -> float:
    """
    Calculate e^x + sqrt(x)
    """
    return math.exp(x) + math.sqrt(x)


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of the digits of an integer
    """
    if isinstance(n, int):
        return sum(int(digit) for digit in str(n))

    raise ValueError(f"Input must be an integer, got {type(n)}")
