def calculate_even_odd():
    even_sum = sum(i for i in range(21) if i % 2 == 0)
    odd_product = 1
    for i in range(1, 21, 2):
        odd_product *= i
    print(f"Sum of even numbers: {even_sum}")
    print(f"Product of odd numbers: {odd_product}")

if __name__ == '__main__':
    calculate_even_odd()
