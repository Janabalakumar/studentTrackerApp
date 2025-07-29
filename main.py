# main.py

import student_db

def menu():
    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Individual Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            s1 = int(input("Enter marks for Subject 1: "))
            s2 = int(input("Enter marks for Subject 2: "))
            s3 = int(input("Enter marks for Subject 3: "))
            s4 = int(input("Enter marks for Subject 4: "))
            s5 = int(input("Enter marks for Subject 5: "))
            student_db.add_student(name, s1, s2, s3, s4, s5)

        elif choice == '2':
            student_db.view_all_students()

        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            student_db.view_student(student_id)

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            student_db.delete_student(student_id)

        elif choice == '5':
            print("Exiting... 👋")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
