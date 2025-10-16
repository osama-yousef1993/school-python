import argparse

from src.courses.courses import Courses
from src.marks.marks import Marks
from src.student.student import Student


def main():
    school_name = "Springfield High"
    parser = argparse.ArgumentParser(
        description=f"Welcome to {school_name} Management System"
    )
    parser.add_argument(
        "--version", action="version", version="School Management System 1.0"
    )
    args = parser.parse_args()
    print(f"{args} this is you arge")
    print(f"{school_name} Management System")
    select_option()


def select_option():
    print("Select an option:")
    print("1. Manage Students")
    print("2. Manage Courses")
    print("3. Manage Marks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        student_manager = Student()
        print("Select an option for Student:")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Fetch Students")
        print("4. Exit")
        student_choice = input("Enter your choice (1-4): ")
        if student_choice == "1":
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            student_data = {"id": student_id, "name": student_name}
            try:
                student_manager.add_student(student_data)
                print("Student added successfully.")
            except ValueError as e:
                print(e)
        elif student_choice == "2":
            student_id = input("Enter Student ID to delete: ")
            try:
                student_manager.delete_student(student_id)
                print("Student deleted successfully.")
            except ValueError as e:
                print(e)
        elif student_choice == "3":
            students = student_manager.get_students()
            for student in students:
                print(f"ID: {student['id']}, Name: {student['name']}")
        print("Student Management Selected")
        # Add further student management logic here
    elif choice == "2":
        course_manager = Courses()
        print("Select an option for Course:")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Fetch Courses")
        print("4. Exit")
        course_choice = input("Enter your choice (1-4): ")
        if course_choice == "1":
            course_name = input("Enter Course Name: ")
            course_data = {"name": course_name}
            try:
                course_manager.add_courses(course_data)
                print("Course added successfully.")
            except ValueError as e:
                print(e)
        elif course_choice == "2":
            course_name = input("Enter Course Name to delete: ")
            try:
                course_manager.delete_course(course_name)
                print("Course deleted successfully.")
            except ValueError as e:
                print(e)
        elif course_choice == "3":
            courses = course_manager.get_courses()
            for course in courses:
                print(f"Course Name: {course['name']}")
        print("Course Management Selected")
        # Add further course management logic here
    elif choice == "3":
        marks_manager = Marks()
        print("Select an option for Marks:")
        print("1. Add Marks")
        print("2. Delete Marks")
        print("3. Fetch Marks")
        print("4. Exit")
        marks_choice = input("Enter your choice (1-4): ")
        if marks_choice == "1":
            student_id = input("Enter Student ID: ")
            course_name = input("Enter Course Name: ")
            mark_value = input("Enter Mark: ")
            mark_data = {
                "student_id": student_id,
                "course_name": course_name,
                "mark": mark_value,
            }
            try:
                marks_manager.add_mark(mark_data)
                print("Mark added successfully.")
            except ValueError as e:
                print(e)
        elif marks_choice == "2":
            student_id = input("Enter Student ID to delete mark: ")
            course_name = input("Enter Course Name to delete mark: ")
            try:
                marks_manager.delete_mark(student_id, course_name)
                print("Mark deleted successfully.")
            except ValueError as e:
                print(e)
        elif marks_choice == "3":
            marks = marks_manager.get_marks()
            for mark in marks:
                print(
                    f"Student ID: {mark['student_id']}, Course Name: {mark['course_name']}, Mark: {mark['mark']}"
                )
        print("Marks Management Selected")
        # Add further marks management logic here
    return choice


if __name__ == "__main__":
    main()
