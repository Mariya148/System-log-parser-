class LogParser:
    def __init__(self, file_path):  # constructor
        self.file_path = file_path
        self.log_counts = {}  # create an empty dictionary to add to it later

    def parse_logs(self):
        with open(self.file_path, "r") as file:  #read from the file 

            for line in file:  # line= 1 row from the file
                words = line.split()
                level = words[2]  # in the file index 2 is always the log level we are looking for

                if level not in self.log_counts:
                    self.log_counts[level] = 1  # if it doesn't exist
                else:
                    self.log_counts[level] += 1  # if it exists add 1

        print(self.log_counts)


parser = LogParser("app.log")  # instantiate the object.. creates an empty self.log_counts dictionary
parser.parse_logs()  #call the method 