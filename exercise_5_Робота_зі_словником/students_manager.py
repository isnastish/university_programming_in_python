def print_all_values(students: dict) -> None:
    """Print all values from the students dictionary."""
    if not students:
        print("No students in the class.")
        return

    sorted_students = sorted(
        students.items(), key=lambda x: x[1]["height"], reverse=True
    )
    for surname, data in sorted_students:
        print(
            f"{surname}: {data['height']} cm"
            + (f", age {data['age']}" if data.get("age") else "")
        )


def add_entry(students: dict) -> None:
    """Add a new student to the dictionary with error handling."""
    try:
        surname = input("Enter student surname: ").strip()
        if not surname or surname in students:
            print("Error: Invalid or existing surname.")
            return

        height = float(input("Enter student height (cm): "))
        if height <= 0 or height in [data["height"] for data in students.values()]:
            print("Error: Invalid or duplicate height.")
            return

        age = input("Enter student age (optional): ").strip()
        students[surname] = {"height": height, "age": int(age) if age else None}
        print(f"Added: {surname}")
    except ValueError:
        print("Error: Invalid input.")


def remove_entry(students: dict) -> None:
    """Remove a student from the dictionary with error handling."""
    if not students:
        print("No students.")
        return

    surname = input("Enter student surname to remove: ").strip()
    if surname not in students:
        print("Error: Student not found.")
        return

    students.pop(surname)
    print(f"Removed: {surname}")


def print_sorted_by_keys(students: dict) -> None:
    """Print dictionary content sorted by keys (surnames)."""
    if not students:
        print("No students.")
        return

    for key in sorted(students.keys()):
        data = students[key]
        print(
            f"{key}: {data['height']} cm"
            + (f", age {data['age']}" if data.get("age") else "")
        )


def find_students_shorter_than(students: dict, new_height: float) -> list[str]:
    """
    Find surnames of all students whose height is less than the new student's height.
    """
    shorter_students = [
        surname for surname, data in students.items() if data["height"] < new_height
    ]
    return shorter_students


def find_insertion_point(students: dict, new_height: float) -> str:
    """
    Find the surname of the student after which the new student should be inserted
    to maintain descending order.
    """
    sorted_students = sorted(
        students.items(), key=lambda x: x[1]["height"], reverse=True
    )

    for surname, data in sorted_students:
        if data["height"] < new_height:
            return surname

    return sorted_students[-1][0] if sorted_students else ""


def find_closest_height(students: dict, new_height: float) -> str:
    """Find the surname of the student whose height differs least from the new student's height."""
    return (
        min(students.items(), key=lambda x: abs(x[1]["height"] - new_height))[0]
        if students
        else ""
    )


def process_new_student(students: dict) -> None:
    """Process tasks for a new student."""
    if not students:
        print("No students.")
        return

    try:
        new_surname = input("Enter new student's surname: ").strip()
        if not new_surname or new_surname in students:
            print("Error: Invalid or existing surname.")
            return

        new_height = float(input("Enter new student's height (cm): "))
        heights = [data["height"] for data in students.values()]

        if new_height <= 0 or new_height in heights:
            print("Error: Invalid or duplicate height.")
            return

        shorter_students = find_students_shorter_than(students, new_height)
        insertion_point = find_insertion_point(students, new_height)
        closest_student = find_closest_height(students, new_height)

        print(
            f"\na) Shorter students: {', '.join(shorter_students) if shorter_students else 'None'}"
        )
        print(f"b) Insert after: {insertion_point}")
        print(
            f"c) Closest height: {closest_student} ({abs(students[closest_student]['height'] - new_height):.2f} cm diff)"
        )

        if input(f"\nAdd '{new_surname}'? (y/n): ").strip().lower() == "y":
            age = input("Enter age (optional): ").strip()
            students[new_surname] = {
                "height": new_height,
                "age": int(age) if age else None,
            }
            print("Added.")
    except ValueError:
        print("Error: Invalid input.")


def main_menu(students: dict) -> None:
    """
    Display main menu and handle user interactions.
    """
    while True:
        print("\n" + "=" * 60)
        print("Students Height Management System")
        print("=" * 60)
        print("1. Print all students")
        print("2. Add new student")
        print("3. Remove student")
        print("4. Print students sorted by surname")
        print("5. Process new student (tasks a, b, c)")
        print("6. Exit")
        print("=" * 60)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print_all_values(students)
        elif choice == "2":
            add_entry(students)
        elif choice == "3":
            remove_entry(students)
        elif choice == "4":
            print_sorted_by_keys(students)
        elif choice == "5":
            process_new_student(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    students = {
        "Petrov": {"height": 185.5, "age": 17},
        "Ivanov": {"height": 182.0, "age": 16},
        "Sidorov": {"height": 180.0, "age": 17},
        "Kozlov": {"height": 178.5, "age": 16},
        "Volkov": {"height": 175.0, "age": 17},
        "Sokolov": {"height": 173.5, "age": 16},
        "Lebedev": {"height": 171.0, "age": 17},
        "Orlov": {"height": 169.5, "age": 16},
        "Volnov": {"height": 167.0, "age": 17},
        "Medvedev": {"height": 165.0, "age": 16},
    }

    main_menu(students)
