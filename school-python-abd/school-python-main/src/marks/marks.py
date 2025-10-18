from src.helpers.file_helpers import FileHelper
from src.helpers.check_files import FileChecker
from src.courses.courses import Courses
from src.student.student import Student


class Marks:
    def __init__(self):
        self.file_helper = FileHelper()
        self.file_name = "marks.json"
        self.file_checker = FileChecker(f"files/{self.file_name}")
        self.file_checker.file_exists()
        self.marks = self.file_helper.read_file(self.file_name)

    def get_marks(self):
        student_manager = Student()
        course_manager = Courses()

        students = student_manager.get_students()
        courses = {c["name"] for c in course_manager.get_courses()} 
        marks = self.marks

        result = []

        for student in students:
            student_courses = [
                {"course_name": m["course_name"], "mark": m["mark"]}
                for m in marks
                if m["student_id"] == student["id"] and m["course_name"] in courses
            ]

            result.append({
                "student_id": student["id"],
                "name": student.get("name"),
                "course_name": student_courses
            })

        return result


    def add_mark(self, mark_data):
        marks = self.marks

        for mark in marks:
            if (
                mark["student_id"] == mark_data["student_id"]
                and mark["course_name"] == mark_data["course_name"]
            ):
                raise ValueError("Mark already exists")
        marks.append(mark_data)

        self.file_helper.write_file(self.file_name, marks)

    def delete_mark(self, student_id, course_name):
        marks = self.marks

        for i, mark in enumerate(marks):
            if mark["student_id"] == student_id and mark["course_name"] == course_name:
                del marks[i]
                self.file_helper.write_file(self.file_name, marks)
                return

        raise ValueError("Mark not found")
