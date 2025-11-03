def sum_even_indices():
    """
    Program to find the sum of all array elements with even indices.
    User inputs the array from keyboard.
    """
    print("Array Even Index Sum Calculator")
    print("-" * 50)
    
    while True:
        try:
            input_str: str = input("Enter integer elements (space or comma separated): ").strip()
            if not input_str:
                print("Error: Please enter at least one element. Please try again.")
                continue
            
            elements = input_str.replace(',', ' ').split()
            arr: list[int] = [int(elem) for elem in elements]
            break
        except ValueError:
            print("Error: Please enter valid integers separated by spaces or commas. Please try again.")
    
    print(f"\nArray: {arr}")
    
    # Calculate sum of elements with even indices
    even_indices: list[int] = [i for i in range(0, len(arr), 2)]
    sum_even: int = sum(arr[i] for i in even_indices)
    
    print(f"\nElements with even indices: {even_indices}")
    print(f"Values at even indices: {[arr[i] for i in even_indices]}")
    print(f"Sum of elements with even indices: {sum_even}")
    print("-" * 50)
    
    return sum_even


sum_even_indices()

