def create_tf12_1(filename: str = "TF12_1.txt") -> None:
    """
    Creates a text file TF12_1 with character strings of different lengths.
    
    Args:
        filename: name of the file to create
    """
    lines = [
        "First line",
        "Second",
        "Third line of text",
        "Fourth",
        "Fifth line with more characters",
        "Sixth",
        "Seventh line",
        "Eighth line with text",
        "Ninth",
        "Tenth line with long text",
        "Eleventh",
        "Twelfth line",
        "Thirteenth line with text",
        "Fourteenth",
        "Fifteenth line"
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        print(f"File {filename} created successfully.")
    except OSError as e:
        print(f"Error creating file {filename}: {e}")


def process_tf12_1_to_tf12_2(input_filename: str = "TF12_1.txt", 
                              output_filename: str = "TF12_2.txt") -> None:
    """
    Reads the content of file TF12_1 and writes it to file TF12_2 by lines:
    in the first - one character, in the second - two characters, ..., in the tenth - ten characters,
    in the eleventh - one character, etc.
    
    Args:
        input_filename: name of the input file
        output_filename: name of the output file
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as e:
        print(f"Error reading file {input_filename}: {e}")
        return
    
    content = content.replace('\n', '')
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            position = 0
            line_length = 1
            
            while position < len(content):
                chars_to_take = min(line_length, len(content) - position)
                line = content[position:position + chars_to_take]
                
                f.write(line + '\n')
                
                position += chars_to_take
                line_length = (line_length % 10) + 1
        
        print(f"File {output_filename} created successfully.")
    except OSError as e:
        print(f"Error writing to file {output_filename}: {e}")


def read_and_print_tf12_2(filename: str = "TF12_2.txt") -> None:
    """
    Reads the content of file TF12_2 and prints it line by line.
    
    Args:
        filename: name of the file to read
    """
    print(f"\nContent of file {filename}:")
    print("-" * 50)
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line_number = 1
            for line in f:
                line_content = line.rstrip('\n')
                print(f"Line {line_number}: {line_content}")
                line_number += 1
    except OSError as e:
        print(f"Error reading file {filename}: {e}")
    
    print("-" * 50)


def main():
    """Main function of the program."""
    print("=" * 50)
    print("Program for processing text files TF12_1 and TF12_2")
    print("=" * 50)
    
    print("\na) Creating file TF12_1...")
    create_tf12_1()
    
    print("\nb) Processing file TF12_1 and creating TF12_2...")
    process_tf12_1_to_tf12_2()
    
    print("\nc) Printing content of file TF12_2...")
    read_and_print_tf12_2()


if __name__ == "__main__":
    main()

