from src.helpers.file_helpers import FileHelper
from src.helpers.check_files import FileChecker


class Marks:
    def __init__(self):
        self.file_helper = FileHelper()
        self.file_name = "marks.json"
        self.file_checker = FileChecker(f"files/{self.file_name}")
        self.file_checker.file_exists()
        self.marks = self.file_helper.read_file(self.file_name)

    def get_marks(self):
        # todo Add courses and student to fetch the data for
        # all students with their marks and courses
        """
        {
        name: 1
        email: 2
        id: 3
        courses: [{course_name: 1, mark: 2}]
        }

        Returns:
            _type_: _description_
        """
        return self.marks

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
