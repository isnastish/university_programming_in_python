def process_string_slicing():
    """
    Function for demonstrating string slicing operations.
    Gets every 3rd character from 4th to 20th position (20th not included).
    """
    sample_string: str = "abcdefghijklmnopqrstuvwxyz1234567890"

    print(f"Sample string: '{sample_string}'")
    print(f"String length: {len(sample_string)}")
    print()

    # Check if string length is sufficient
    if len(sample_string) < 20:
        print("Error: String length is less than 20 characters")
        print("Cannot perform the slicing operation")
        return

    sliced_string = sample_string[3:19:3]

    print("Slicing operation: string[3:19:3]")
    print(f"Result: '{sliced_string}'")
    print()

    for i in range(3, 19, 3):
        char: str = sample_string[i]
        position: int = i + 1
        print(f"  Position {position}: '{char}' (index {i})")

    print("-" * 50)


def find_largest_digit(n: int) -> int:
    """
    Find the largest digit in a four-digit natural number.
    """
    if not (1000 <= n <= 9999):
        raise ValueError("Number must be a four-digit natural number (1000-9999)")

    digits_str: str = str(n)

    max_digit: int = max(int(digit) for digit in digits_str)

    return max_digit


def find_shortest_word_length(sentence: str) -> int:
    """
    Find the length of the shortest word in a sentence.
    """
    if not sentence.strip():
        return 0

    # Split sentence into words and filter out empty strings
    words = [word.strip() for word in sentence.split() if word.strip()]

    if not words:
        return 0

    # Find the shortest word length
    shortest_length = min(len(word) for word in words)

    return shortest_length


def test_find_largest_digit():
    test_numbers = [1234, 9876, 5555, 1000, 9999]
    for num in test_numbers:
        try:
            largest = find_largest_digit(num)
            print(f"Number: {num} -> Largest digit: {largest}")
        except ValueError as e:
            print(f"Error with {num}: {e}")


def test_find_shortest_word_length():
    test_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a great programming language",
        "Hello world",
        "a",
        "This is a very long sentence with many different words",
        "   ",
        "",
        "One two three four five",
    ]

    for sentence in test_sentences:
        length = find_shortest_word_length(sentence)
        print(f"Sentence: '{sentence}' -> Shortest word length: {length}")


if __name__ == "__main__":
    process_string_slicing()
    # test_find_largest_digit()
    # test_find_shortest_word_length()
