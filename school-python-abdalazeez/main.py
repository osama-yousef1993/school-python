from src.courses.courses import Courses
from src.marks.marks import Marks
from src.student.student import Student
import re
import argparse
import datetime


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

    def validate_name(name):
        name = re.sub(r'[^a-zA-Z\s]', '', name)
        return name
    
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
            student_name = validate_name(input("Enter Student Name: "))
            
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
            if students is None:
                print("No students available.")
            else:
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
            course_name = validate_name(input("Enter Course Name: "))
            course_data = {"name": course_name, "start_date": str(datetime.date.today()),"End Date": "" ,"Capacity": 0}
            try:
                course_manager.add_courses(course_data)
                print("Course added successfully.")
            except ValueError as e:
                print(e)
        elif course_choice == "2":
            course_name = validate_name(input("Enter Course Name to delete: "))
            try:
                course_manager.delete_course(course_name)
                print("Course deleted successfully.")
            except ValueError as e:
                print(e)
        elif course_choice == "3":
            courses = course_manager.get_courses()
            if courses is None:
                print("No courses available.")
            else:
                for course in courses:
                    print(f"Course Name: {course['name']}")
        print("Course Management Selected")
            

    elif choice == "3":
        marks_manager = Marks()
        course_manager = Courses()
        courses = course_manager.get_courses()

        print("Select an option for Marks:")
        print("1. Add Marks")
        print("2. Delete Marks")
        print("3. Fetch Marks")
        print("4. Exit")
        marks_choice = input("Enter your choice (1-4): ")
        if marks_choice == "1":
            student_id = input("Enter Student ID: ")
            course_name = validate_name(input("Enter Course Name: "))
            mark_value = input("Enter Mark: ")
            mark_data = {
                "student_id": student_id,
                "course_name": course_name,
                "mark": mark_value
            }
            try:
                if(course_manager.increase_capacity(course_name) == False):
                    for course in courses:
                        if course["name"] == course_name:
                            course["End Date"] = str(datetime.date.today())
                            course_manager.write_courses()
                    print("Course capacity full. Cannot add more marks.")
                    return
                else:
                    marks_manager.add_mark(mark_data)
                    course_manager.increase_capacity(course_name)
                    print("Mark added successfully.")
            except ValueError as e:
                print(e)
        elif marks_choice == "2":
            student_id = input("Enter Student ID to delete mark: ")
            course_name = validate_name(input("Enter Course Name to delete mark: "))
            try:
                marks_manager.delete_mark(student_id, course_name)
                print("Mark deleted successfully.")
            except ValueError as e:
                print(e)
        elif marks_choice == "3":
            marks = marks_manager.get_marks()

            grouped = {}
            for mark in marks:
                sid = mark['student_id']
                course_info = {
                    'course_name': mark['course_name'],
                    'mark': mark['mark']
                }

                if sid not in grouped:
                    grouped[sid] = {
                        'student_id': sid,
                        'courses': []
                    }
                grouped[sid]['courses'].append(course_info)

            for student in grouped.values():
                print(f"Student ID: {student['student_id']}")
                for course in student['courses']:
                    status = "pass" if int(course['mark']) >= 50 else "fail"
                    print(f"  Course: {course['course_name']}, Mark: {status}")

             
        print("Marks Management Selected")
    return choice    


if __name__ == "__main__":
    main()
