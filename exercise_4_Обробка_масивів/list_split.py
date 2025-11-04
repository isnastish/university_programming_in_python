def split_list_by_value():
    """
    Split a list into two lists based on a specified split value.
    User inputs the list and split value from keyboard.
    """
    while True:
        try:
            input_str: str = input("Enter list elements: ").strip()
            elements = input_str.replace(",", " ").split()
            user_list: list[int] = [int(elem) for elem in elements]
            break
        except ValueError:
            print("Error: Invalid input. Please try again.")

    while True:
        try:
            split_value: int = int(input("Enter split value: "))
            break
        except ValueError:
            print("Error: Invalid input. Please try again.")

    list_less: list[int] = [elem for elem in user_list if elem < split_value]
    list_greater_equal: list[int] = [elem for elem in user_list if elem >= split_value]

    print(f"List 1: {list_less}")
    print(f"List 2: {list_greater_equal}")

    return list_less, list_greater_equal


split_list_by_value()
