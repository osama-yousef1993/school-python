from src.helpers.check_files import FileChecker
from src.helpers.file_helpers import FileHelper


class Courses:
    def __init__(self):
        self.file_helper = FileHelper()
        self.file_name = "courses.json"
        self.file_checker = FileChecker(f"files/{self.file_name}")
        self.file_checker.file_exists()
        self.courses = self.file_helper.read_file(self.file_name)

    def get_courses(self):
        return self.courses

    def add_courses(self, course_data):
        courses = self.courses

        for course in courses:
            if course["name"] == course_data["name"]:
                raise ValueError("Course already exists")
        courses.append(course_data)

        self.file_helper.write_file(self.file_name, courses)

    def delete_course(self, course_name):
        courses = self.courses

        for i, course in enumerate(courses):
            if course["name"] == course_name:
                del courses[i]
                self.file_helper.write_file(self.file_name, courses)
                return

        raise ValueError("Course not found")
