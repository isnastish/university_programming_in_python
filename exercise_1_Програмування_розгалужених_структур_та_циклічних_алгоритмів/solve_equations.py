def solve_equation(a: float, b: float) -> float:
    """
    Solve: x = { b*a + 1, if a > b; -10 if a = b; (a - 5) / b if a < b; }
    """
    if a > b:
        return b * a + 1
    if a == b:
        return -10
    if a < b:
        if b == 0:
            raise ZeroDivisionError(f"Division by zero: {b}")
        return (a - 5) / b
    return 0


# Test cases
if __name__ == "__main__":
    test_cases = [(10, 5), (7, 7), (3, 8), (-3, 0)]
    for a, b in test_cases:
        try:
            x = solve_equation(a, b)
            print(f"a={a}, b={b} → x={x}")
        except ZeroDivisionError:
            print(f"a={a}, b={b} → Error: Division by zero")
