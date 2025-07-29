# student_db.py

import mysql.connector
import db_config

def connect_db():
    return mysql.connector.connect(
        host=db_config.host,
        user=db_config.user,
        password=db_config.password,
        database=db_config.database
    )

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 45:
        return 'D'
    else:
        return 'F'

def add_student(name, s1, s2, s3, s4, s5):
    total = s1 + s2 + s3 + s4 + s5
    avg = total / 5
    grade = calculate_grade(avg)

    con = connect_db()
    cur = con.cursor()
    query = "INSERT INTO students (name, subject1, subject2, subject3, subject4, subject5, total, average, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, s1, s2, s3, s4, s5, total, avg, grade)
    cur.execute(query, values)
    con.commit()
    con.close()
    print("✅ Student added successfully.")

def view_all_students():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    records = cur.fetchall()
    con.close()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Total: {row[7]}, Average: {row[8]:.2f}, Grade: {row[9]}")

def view_student(student_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    record = cur.fetchone()
    con.close()
    if record:
        print(f"ID: {record[0]}, Name: {record[1]}")
        print(f"Subjects: {record[2]}, {record[3]}, {record[4]}, {record[5]}, {record[6]}")
        print(f"Total: {record[7]}, Average: {record[8]:.2f}, Grade: {record[9]}")
    else:
        print("❌ Student not found.")

def delete_student(student_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    con.commit()
    con.close()
    print("🗑️ Student record deleted.")
