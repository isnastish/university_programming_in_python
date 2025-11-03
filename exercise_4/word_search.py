def search_word_in_list():
    """
    Search for a word in a list and print the result.
    User inputs the list and search word from keyboard.
    """
    while True:
        try:
            input_str: str = input("Enter list elements: ").strip()
            elements = input_str.replace(',', ' ').split()
            user_list: list[str] = [elem.strip() for elem in elements]
            break
        except Exception:
            print("Error: Invalid input. Please try again.")
    
    search_word: str = input("Enter word to search: ").strip()
    
    print(f"List: {user_list}")
    
    if search_word in user_list:
        index: int = user_list.index(search_word)
        print(f"Word '{search_word}' found at index {index}")
    else:
        print(f"Word '{search_word}' not found in the list")
    
    return search_word in user_list


def test_search_word():
    """Simple tests for word search function."""
    test_list1 = ["apple", "banana", "cherry"]
    word1 = "banana"
    assert word1 in test_list1, f"Test 1 failed: '{word1}' should be found in {test_list1}"
    print(f"✓ Test 1 passed: '{word1}' found in {test_list1}")
    
    test_list2 = ["apple", "banana", "cherry"]
    word2 = "orange"
    assert word2 not in test_list2, f"Test 2 failed: '{word2}' should not be found in {test_list2}"
    print(f"✓ Test 2 passed: '{word2}' not found in {test_list2}")
    
    test_list3 = []
    word3 = "test"
    assert word3 not in test_list3, f"Test 3 failed: '{word3}' should not be found in empty list"
    print(f"✓ Test 3 passed: '{word3}' not found in empty list")
    
    test_list4 = ["first", "second", "third"]
    word4 = "first"
    assert test_list4.index(word4) == 0, f"Test 4 failed: '{word4}' should be at index 0"
    print(f"✓ Test 4 passed: '{word4}' found at index 0")
    
    test_list5 = ["Apple", "Banana"]
    word5 = "apple"
    assert word5 not in test_list5, f"Test 5 failed: Case sensitive search should not find '{word5}'"
    print("✓ Test 5 passed: Case sensitive search works correctly")
    
    print("\nAll tests passed!")


test_search_word()

