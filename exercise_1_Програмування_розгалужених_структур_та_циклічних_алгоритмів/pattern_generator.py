def generate_pattern(n):
    """
    Generate a diamond pattern with number n.
    Example for n=5:
    5 5 5 5 5
    5 5 5 5
    5 5 5
    5 5
    5
    5 5
    5 5 5
    5 5 5 5
    5 5 5 5 5
    """
    for i in range(n, 0, -1):
        print(" ".join([str(n)] * i))

    for i in range(2, n + 1):
        print(" ".join([str(n)] * i))


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter N (1 < N < 9) or 'quit' to exit: "))
            if 1 < n < 9:
                generate_pattern(n)
                break
            else:
                print("N must be between 2 and 8")
        except ValueError:
            user_input = input("Enter N (1 < N < 9) or 'quit' to exit: ")
            if user_input.lower() == "quit":
                break
            print("Please enter a valid integer")
