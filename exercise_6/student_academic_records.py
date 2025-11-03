"""
Program for working with dictionary of student academic performance in a group.
Author: Yevtushenko Oleksii

Dictionary structure:
- key: student surname (string)
- value: dictionary with data:
  - 'group': group number (string)
  - 'full_name': full name (dictionary: 'surname', 'first_name', 'patronymic')
  - 'course': course number (integer)
  - 'subjects': dictionary of subjects and grades {subject: grade}
  - 'average': average grade (float, calculated automatically)
"""


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
        
        # Enter group number
        group = input("Enter group number: ").strip()
        if not group:
            print("Error: Group number cannot be empty.")
            return
        
        # Enter full name
        first_name = input("Enter first name: ").strip()
        if not first_name:
            print("Error: First name cannot be empty.")
            return
        
        patronymic = input("Enter patronymic: ").strip()
        
        # Enter course
        course = int(input("Enter course: "))
        if course < 1 or course > 6:
            print("Error: Course must be between 1 and 6.")
            return
        
        # Enter subjects and grades
        subjects = {}
        print("Enter subjects and grades (type 'end' to finish):")
        while True:
            subject = input("Subject name: ").strip()
            if subject.lower() == 'end':
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
        
        # Calculate average grade
        average = sum(subjects.values()) / len(subjects)
        
        # Add student to dictionary
        students[surname] = {
            'group': group,
            'full_name': {
                'surname': surname,
                'first_name': first_name,
                'patronymic': patronymic
            },
            'course': course,
            'subjects': subjects,
            'average': round(average, 2)
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
        full_name = data['full_name']
        name_str = f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        subjects_str = ", ".join([f"{s}: {g}" for s, g in data['subjects'].items()])
        print(f"{surname} {name_str} - Group: {data['group']}, Course: {data['course']}, Avg: {data['average']} | {subjects_str}")


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
    
    sorted_students = sorted(students.items(), key=lambda x: x[1]['average'], reverse=True)
    for surname, data in sorted_students:
        full_name = data['full_name']
        name_str = f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        print(f"{surname} {name_str}: {data['average']} (group {data['group']}, course {data['course']})")


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
        (surname, data) for surname, data in students.items()
        if data['group'] == group
    ]
    
    if not found_students:
        print(f"Group '{group}' not found.")
        return
    
    print(f"Group '{group}':")
    for surname, data in found_students:
        full_name = data['full_name']
        name_str = f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        print(f"  {surname} {name_str} - course {data['course']}, avg: {data['average']}")


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
        full_name = data['full_name']
        name_str = f"{full_name['first_name']} {full_name.get('patronymic', '')}".strip()
        print(f"{key} {name_str} - Group: {data['group']}, Course: {data['course']}, Average: {data['average']}")


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
    
    group_averages = [data['average'] for surname, data in students.items() if data['group'] == group]
    
    if not group_averages:
        print(f"Group '{group}' not found.")
        return
    
    group_average = sum(group_averages) / len(group_averages)
    print(f"Group '{group}' average: {round(group_average, 2)} ({len(group_averages)} students)")


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
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            display_sorted_by_keys(students)
        elif choice == '4':
            sort_students_by_average(students)
        elif choice == '5':
            find_students_by_group(students)
        elif choice == '6':
            calculate_group_average(students)
        elif choice == '7':
            remove_student(students)
        elif choice == '8':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    # Initialize dictionary with sample data
    # Author: Yevtushenko Oleksii
    students = {
        'Petrenko': {
            'group': 'IP-21',
            'full_name': {
                'surname': 'Petrenko',
                'first_name': 'Oleksandr',
                'patronymic': 'Ivanovych'
            },
            'course': 2,
            'subjects': {
                'Mathematics': 85,
                'Programming': 92,
                'Physics': 78,
                'English': 88
            },
            'average': 85.75
        },
        'Kovalenko': {
            'group': 'IP-21',
            'full_name': {
                'surname': 'Kovalenko',
                'first_name': 'Maria',
                'patronymic': 'Petrivna'
            },
            'course': 2,
            'subjects': {
                'Mathematics': 95,
                'Programming': 98,
                'Physics': 90,
                'English': 92
            },
            'average': 93.75
        },
        'Sydorenko': {
            'group': 'IP-22',
            'full_name': {
                'surname': 'Sydorenko',
                'first_name': 'Dmytro',
                'patronymic': 'Oleksandrovych'
            },
            'course': 1,
            'subjects': {
                'Mathematics': 75,
                'Programming': 80,
                'Physics': 70,
                'English': 78
            },
            'average': 75.75
        },
        'Ivanenko': {
            'group': 'IP-21',
            'full_name': {
                'surname': 'Ivanenko',
                'first_name': 'Anna',
                'patronymic': 'Serhiivna'
            },
            'course': 2,
            'subjects': {
                'Mathematics': 88,
                'Programming': 85,
                'Physics': 82,
                'English': 90
            },
            'average': 86.25
        },
        'Melnyk': {
            'group': 'IP-22',
            'full_name': {
                'surname': 'Melnyk',
                'first_name': 'Volodymyr',
                'patronymic': 'Mykolayovych'
            },
            'course': 1,
            'subjects': {
                'Mathematics': 90,
                'Programming': 88,
                'Physics': 85,
                'English': 87
            },
            'average': 87.5
        }
    }
    
    main_menu(students)
