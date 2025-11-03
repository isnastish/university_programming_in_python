import json
import os


def add_student(students: dict) -> None:
    """
    Add a new student to the dictionary.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    try:
        # Enter surname (dictionary key)
        surname = input("Enter student surname: ").strip()
        if not surname:
            print("Error: Surname cannot be empty.")
            return

        if surname in students:
            print(f"Error: Student with surname '{surname}' already exists.")
            return

        group = input("Enter group number: ").strip()
        if not group:
            print("Error: Group number cannot be empty.")
            return
        first_name = input("Enter first name: ").strip()
        if not first_name:
            print("Error: First name cannot be empty.")
            return

        patronymic = input("Enter patronymic: ").strip()

        course = int(input("Enter course: "))
        if course < 1 or course > 6:
            print("Error: Course must be between 1 and 6.")
            return
        subjects = {}
        print("Enter subjects and grades (type 'end' to finish):")
        while True:
            subject = input("Subject name: ").strip()
            if subject.lower() == "end":
                break
            if not subject:
                continue

            try:
                grade = float(input(f"Grade for '{subject}': "))
                if grade < 0 or grade > 100:
                    print("Error: Grade must be between 0 and 100.")
                    continue
                subjects[subject] = grade
            except ValueError:
                print("Error: Enter a valid grade.")

        if not subjects:
            print("Error: At least one subject with grade must be entered.")
            return

        average = sum(subjects.values()) / len(subjects)

        students[surname] = {
            "group": group,
            "full_name": {
                "surname": surname,
                "first_name": first_name,
                "patronymic": patronymic,
            },
            "course": course,
            "subjects": subjects,
            "average": round(average, 2),
        }

        print(f"Added: {surname}")
    except ValueError:
        print("Error: Invalid input.")
    except Exception as e:
        print(f"Error: {e}")


def display_all_students(students: dict) -> None:
    """
    Display all values from the dictionary.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    if not students:
        print("No students.")
        return

    for surname, data in students.items():
        full_name = data["full_name"]
        name_str = (
            f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        )
        subjects_str = ", ".join([f"{s}: {g}" for s, g in data["subjects"].items()])
        print(
            f"{surname} {name_str} - Group: {data['group']}, Course: {data['course']}, Avg: {data['average']} | {subjects_str}"
        )


def sort_students_by_average(students: dict) -> None:
    """
    Sort dictionary data by average grade (descending).
    Author: Yevtushenko Oleksii

    Function displays students sorted by average grade,
    from highest to lowest.

    Args:
        students: dictionary with student data
    """
    if not students:
        print("No students.")
        return

    sorted_students = sorted(
        students.items(), key=lambda x: x[1]["average"], reverse=True
    )
    for surname, data in sorted_students:
        full_name = data["full_name"]
        name_str = (
            f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        )
        print(
            f"{surname} {name_str}: {data['average']} (group {data['group']}, course {data['course']})"
        )


def find_students_by_group(students: dict) -> None:
    """
    Search for students by group number.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    if not students:
        print("Dictionary is empty.")
        return
    group = input("Enter group number to search: ").strip()
    if not group:
        print("Error: Group number cannot be empty.")
        return

    # Search students by group
    found_students = [
        (surname, data) for surname, data in students.items() if data["group"] == group
    ]

    if not found_students:
        print(f"Group '{group}' not found.")
        return

    print(f"Group '{group}':")
    for surname, data in found_students:
        full_name = data["full_name"]
        name_str = (
            f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        )
        print(
            f"  {surname} {name_str} - course {data['course']}, avg: {data['average']}"
        )


def display_sorted_by_keys(students: dict) -> None:
    """
    View dictionary content sorted by keys (surnames).
    Author: Yevtushenko Oleksii

    Uses sorted() function to sort keys.

    Args:
        students: dictionary with student data
    """
    if not students:
        print("No students.")
        return

    for key in sorted(students.keys()):
        data = students[key]
        full_name = data["full_name"]
        name_str = (
            f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        )
        print(
            f"{key} {name_str} - Group: {data['group']}, Course: {data['course']}, Average: {data['average']}"
        )


def remove_student(students: dict) -> None:
    """
    Remove a student record from the dictionary.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    if not students:
        print("No students.")
        return
    surname = input("Enter student surname to remove: ").strip()
    if not surname or surname not in students:
        print("Error: Student not found.")
        return
    students.pop(surname)
    print(f"Removed: {surname}")


def calculate_group_average(students: dict) -> None:
    """
    Calculate average grade for a group.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    if not students:
        print("No students.")
        return
    group = input("Enter group number: ").strip()
    if not group:
        print("Error: Invalid input.")
        return

    group_averages = [
        data["average"] for surname, data in students.items() if data["group"] == group
    ]

    if not group_averages:
        print(f"Group '{group}' not found.")
        return

    group_average = sum(group_averages) / len(group_averages)
    print(
        f"Group '{group}' average: {round(group_average, 2)} ({len(group_averages)} students)"
    )


def main_menu(students: dict) -> None:
    """
    Main menu for working with dictionary.
    Author: Yevtushenko Oleksii
    Args:
        students: dictionary with student data
    """
    while True:
        print("\n" + "=" * 80)
        print("STUDENT ACADEMIC PERFORMANCE MANAGEMENT SYSTEM")
        print("=" * 80)
        print("1. Add new student")
        print("2. Display all students")
        print("3. Display students sorted by surname")
        print("4. Display students sorted by average grade")
        print("5. Find students by group")
        print("6. Calculate group average grade")
        print("7. Remove student")
        print("8. Exit")
        print("=" * 80)

        choice = input("Enter your choice (1-8): ").strip()

        match choice:
            case "1":
                add_student(students)
            case "2":
                display_all_students(students)
            case "3":
                display_sorted_by_keys(students)
            case "4":
                sort_students_by_average(students)
            case "5":
                find_students_by_group(students)
            case "6":
                calculate_group_average(students)
            case "7":
                remove_student(students)
            case "8":
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    json_file = os.path.join(os.path.dirname(__file__), "students_data.json")

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            students = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        students = {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{json_file}'.")
        students = {}
    except Exception as e:
        print(f"Error loading data: {e}")
        students = {}

    main_menu(students)
