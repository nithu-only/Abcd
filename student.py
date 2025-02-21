import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT
    )
''')

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    cursor.execute('''
        INSERT INTO students (name, age, course) VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f"Added new student: {name}")

def list_students_in_course():
    course = input("Enter the course name to list students: ")
    print(f"\nStudents enrolled in {course}:")
    cursor.execute('''
        SELECT id, name, age FROM students WHERE course = ?
    ''', (course,))
    students = cursor.fetchall()
    if students:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
    else:
        print(f"No students enrolled in {course}.")

def update_student_age():
    student_id = int(input("Enter the student ID to update age: "))
    new_age = int(input(f"Enter the new age for student ID {student_id}: "))
    
    cursor.execute('''
        SELECT * FROM students WHERE id = ?
    ''', (student_id,))
    student = cursor.fetchone()

    if student:
        cursor.execute('''
            UPDATE students SET age = ? WHERE id = ?
        ''', (new_age, student_id))
        conn.commit()
        print(f"Updated student ID {student_id}'s age to {new_age}.")
    else:
        print(f"Student with ID {student_id} not found.")
#menu for prompt
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. List all students in a course")
        print("3. Update a student's age")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            list_students_in_course()
        elif choice == '3':
            update_student_age()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")
main_menu()
conn.close()
