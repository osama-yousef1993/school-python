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
        courses = course_manager.get_courses()
        marks = self.marks

        result = []
        for student in students:
            student_courses = []
            for mark in marks:
                if mark["student_id"] == student["id"]:
                    if any(c["name"] == mark["course_name"] for c in courses):
                        student_courses.append(
                            {"course_name": mark["course_name"], "mark": mark["mark"]}
                        )
            result.append(
                {
                    "student_id": student["id"],
                    "name": student.get("name"),
                    "course_name": student_courses,
                }
            )
            
        return result

    def add_mark(self, mark_data):
        marks = self.marks
        course_manager = Courses()
        student_manager = Student()

        courses = course_manager.get_courses()
        students = student_manager.get_students()

        if not any(c["name"] == mark_data["course_name"] for c in courses):
            raise ValueError("Course does not exist")

        if not any(s["id"] == mark_data["student_id"] for s in students):
            raise ValueError("Student does not exist")

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
