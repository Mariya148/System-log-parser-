class LogParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_logs(self):
        with open(self.file_path, "r") as file:
            content = file.read()
            print(content)

parser = LogParser("app.log")
parser.parse_logs()