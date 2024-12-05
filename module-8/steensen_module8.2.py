# Alisa Steensen
# Module 8.2

# Import json file and display list of students before addition of new student, add new student to the list
# Then display the updated list to the json file

import json

def load_json_file(filename):
    """Load the JSON file into a Python list."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return []

def print_students(student_list, message):
    """Loop through the class list and print."""
    print(f"\n{message}")
    for student in student_list:
        print(f"{student['F_Name']} {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

def update_json_file(filename, student_list):
    """Write the updated class list back to the JSON file."""
    with open(filename, 'w') as f:
        json.dump(student_list, f, indent=4)
    print("\nThe JSON file has been updated.")

def main():
    """Main function of the program and addition of the new student to list."""
    filename = 'student.json'

    # Loading Json file
    students = load_json_file(filename)

    # Print original student list
    print_students(students, "This is the original Student List")

    # New Student in list
    new_student = {
        "F_Name": "Alisa",
        "L_Name": "Steensen",
        "Student_ID": 12345,
        "Email": "alisasteensen@gmail.com"
    }
    students.append(new_student)

    # Update student list
    print_students(students, "This is the updated Student List")

    # Update the JSON file
    update_json_file(filename, students)

if __name__ == '__main__':
    main()
