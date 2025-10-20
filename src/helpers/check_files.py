import os


class FileChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self):
        check = os.path.isfile(self.file_path)
        if not check:
            if os.path.exists(self.file_path):
                os.mkdir(os.path.dirname(self.file_path))
            with open(self.file_path, "w") as file:
                file.write("[]")
        return check
