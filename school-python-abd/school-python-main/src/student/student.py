from src.helpers.file_helpers import FileHelper
from src.helpers.check_files import FileChecker


class Student:
    def __init__(self):
        self.file_helper = FileHelper()
        self.file_name = "students.json"
        self.file_checker = FileChecker(f"files/{self.file_name}")
        self.file_checker.file_exists()
        self.students = self.file_helper.read_file(self.file_name)
        
    def get_students(self):
        return self.students

    def add_student(self, student_data):
        students = self.students

        for student in students:
            if student["id"] == student_data["id"]:
                raise ValueError("Student already exists")
        students.append(student_data)

        self.file_helper.write_file(self.file_name, students)

    def delete_student(self, student_id):
        students = self.students

        for i, student in enumerate(students):
            if student["id"] == student_id:
                del students[i]
                self.file_helper.write_file(self.file_name, students)
                return

        raise ValueError("Student not found")
