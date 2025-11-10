def create_checkerboard_array():
    """
    Create and display a 7x7 checkerboard pattern array.
    Pattern: 1 at positions where (row + col) is even, 0 otherwise.
    """
    # Initialize 7x7 array
    size: int = 7
    arr: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]

    # Fill in the array with data
    for i in range(size):
        for j in range(size):
            arr[i][j] = 1 if (i + j) % 2 == 0 else 0

    # Display the array
    print("7x7 Checkerboard Array:")
    print("-" * 25)
    for i in range(size):
        for j in range(size):
            print(arr[i][j], end=" ")
        print()
    print("-" * 25)

    return arr


create_checkerboard_array()
