"""
Collaborative Task: Creating and updating a shared text file.
Students take turns answering questions and posing new ones.
"""

import os

COLLABORATIVE_FILE = "collaborative_qa.txt"


# STUDENT 1: Yevtushenko Oleksii - created initial file
def create_initial_file(surname: str, question: str) -> None:
    """Creates the initial text file with surname and question."""
    try:
        if os.path.exists(COLLABORATIVE_FILE):
            print(f"File '{COLLABORATIVE_FILE}' already exists!")
            return

        with open(COLLABORATIVE_FILE, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write("STUDENT COLLABORATION: PYTHON Q&A\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"--- STUDENT 1: {surname} ---\n\n")
            f.write(f"QUESTION: {question}\n\n")

        print(f"File created! Question: {question}")
    except OSError as e:
        print(f"Error: {e}")


# STUDENT 2+ : Adds answer and new question
def add_answer_and_question(
    surname: str, answer: str, new_question: str | None = None
) -> None:
    """Adds an answer to the previous question and a new question."""
    try:
        if not os.path.exists(COLLABORATIVE_FILE):
            print(f"Error: File '{COLLABORATIVE_FILE}' not found!")
            return

        with open(COLLABORATIVE_FILE, "a", encoding="utf-8") as f:
            f.write("-" * 60 + "\n")
            f.write(f"--- STUDENT: {surname} ---\n\n")
            f.write("ANSWER:\n")
            for line in answer.strip().split("\n"):
                f.write(f"  {line}\n")
            f.write("\n")
            if new_question:
                f.write(f"QUESTION: {new_question}\n\n")

        print(f"Answer from {surname} added!")
    except OSError as e:
        print(f"Error: {e}")


def display_file() -> None:
    """Displays the file content."""
    try:
        with open(COLLABORATIVE_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # STUDENT 1: Yevtushenko Oleksii
    if not os.path.exists(COLLABORATIVE_FILE):
        create_initial_file(
            "Yevtushenko Oleksii",
            "What is list comprehension in Python and provide an example?",
        )

    # STUDENT 2: Yevtushenko Oleksii - added answer and question
    add_answer_and_question(
        "Surname Name",
        "List comprehension is a compact way to create lists.\nExample: squares = [x**2 for x in range(10)]",
        "What is the difference between list and tuple?"
    )

    # STUDENT 3: Yevtushenko Oleksii - added answer and question
    # add_answer_and_question(
    #     "Surname Name",
    #     "Your answer here...",
    #     "Your question here..."
    # )

    display_file()
