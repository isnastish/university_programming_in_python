import json
from typing import List, Dict, Any


def read_json_file(filename: str) -> List[Dict[str, Any]]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def write_json_file(filename: str, data: List[Dict[str, Any]]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def display_json_content(data: List[Dict[str, Any]]) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def add_student(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    name = input("Enter student name: ").strip()
    if not name:
        return data

    gender = input("Enter gender (male/female): ").strip().lower()
    if gender not in ["male", "female"]:
        return data

    try:
        height = float(input("Enter height (cm): "))
        if height <= 0:
            return data
    except ValueError:
        return data

    data.append({"name": name, "gender": gender, "height": height})
    data.sort(key=lambda x: x["height"], reverse=True)
    return data


def remove_student(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for i, student in enumerate(data, 1):
        print(f"{i}. {student['name']} ({student['gender']}) - {student['height']} cm")

    try:
        index = int(input("Enter student number to remove: ")) - 1
        if 0 <= index < len(data):
            data.pop(index)
    except (ValueError, IndexError):
        pass

    return data


def search_students(data: List[Dict[str, Any]]) -> None:
    print("1. Name 2. Gender 3. Height (exact) 4. Height (range)")
    choice = input("Enter choice: ").strip()
    results = []

    if choice == "1":
        search_term = input("Enter name: ").strip().lower()
        results = [s for s in data if search_term in s["name"].lower()]

    elif choice == "2":
        gender = input("Enter gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            results = [s for s in data if s["gender"] == gender]

    elif choice == "3":
        try:
            height = float(input("Enter height: "))
            results = [s for s in data if s["height"] == height]
        except ValueError:
            return

    elif choice == "4":
        try:
            min_height = float(input("Min height: "))
            max_height = float(input("Max height: "))
            results = [s for s in data if min_height <= s["height"] <= max_height]
        except ValueError:
            return

    for student in results:
        print(f"{student['name']} ({student['gender']}) - {student['height']} cm")


def calculate_height_comparison(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    girls_height = sum(s["height"] for s in data if s["gender"] == "female")
    boys_height = sum(s["height"] for s in data if s["gender"] == "male")

    return {
        "total_girls_height": girls_height,
        "total_boys_height": boys_height,
        "girls_exceed_boys": girls_height > boys_height,
        "difference": abs(girls_height - boys_height),
        "girls_count": sum(1 for s in data if s["gender"] == "female"),
        "boys_count": sum(1 for s in data if s["gender"] == "male"),
    }


def main():
    filename = "students_data.json"
    result_filename = "height_comparison_result.json"
    data = read_json_file(filename)

    while True:
        print("\n1. Display 2. Add 3. Remove 4. Search 5. Calculate 6. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            display_json_content(data)
        elif choice == "2":
            data = add_student(data)
            write_json_file(filename, data)
        elif choice == "3":
            data = remove_student(data)
            write_json_file(filename, data)
        elif choice == "4":
            search_students(data)
        elif choice == "5":
            result = calculate_height_comparison(data)
            print(f"Girls: {result['total_girls_height']:.2f} cm")
            print(f"Boys: {result['total_boys_height']:.2f} cm")
            print(f"Girls exceed: {'Yes' if result['girls_exceed_boys'] else 'No'}")
            write_json_file(result_filename, [result])
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
