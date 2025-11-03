def add_digits_to_char_set():
    """
    Add set of all digits to a character set {c, d}.
    """
    char_set = {'c', 'd'}
    digits_set = {str(i) for i in range(10)}
    
    result_set = char_set | digits_set
    
    print(f"Character set: {char_set}")
    print(f"Digits set: {digits_set}")
    print(f"Result set: {result_set}")
    
    return result_set


add_digits_to_char_set()

