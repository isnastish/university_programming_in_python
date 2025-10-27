from my_math_module import sum_of_digits, compute_expression


def process_sum_of_digits():
    print("Sum of Digits Calculator")
    print("Enter numbers to calculate sum of digits (type 'quit' to exit)")
    print("-" * 40)

    while True:
        try:
            user_input = input("Enter a number: ").strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            number = int(user_input)
            result = sum_of_digits(number)

            print(f"For number {number}")
            print(f"Sum of digits = {result}")
            print("-" * 40)
        except ValueError:
            print("Error: Please enter a valid integer or 'quit' to exit")
            print("Please try again.\n")
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def process_compute_expression():
    print("Calculator for z = e^x + sqrt(x)")
    print("Enter numbers to calculate (type 'quit' to exit)")
    print("-" * 40)

    while True:
        try:
            user_input = input("Enter value for x: ").strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            x = float(user_input)

            if x < 0:
                print("Error: x must be a non-negative number (x >= 0)")
                print("Please try again.\n")
                continue

            z = compute_expression(x)

            print(f"For x = {x}")
            print(f"z = e^{x} + sqrt({x}) = {z:.6f}")
            print("-" * 40)
        except ValueError:
            print("Error: Please enter a numeric value or 'quit' to exit")
            print("Please try again.\n")
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    process_sum_of_digits()
    # process_compute_expression()
