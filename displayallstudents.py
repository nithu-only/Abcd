import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""SELECT * FROM students""")


students = cursor.fetchall()
print("Student Records in Database:")
for student in students:
    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")

conn.close()
