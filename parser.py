class LogParser:
    def __init__(self, file_path):  # constructor
        self.file_path = file_path
        self.log_counts = {}  # create an empty dictionary to add to it later
        self.time_stamps = []  # create a list for the time stamps
        self.error_details = []  # empty list

    def parse_logs(self):
        with open(self.file_path, "r") as file:  #read from the file 

            for line in file:  # line= 1 row from the file
                words = line.split()  # cut the string whenever there's a space
                level = words[2]  # in the file index 2 is always the log level we are looking for

                if level == "[ERROR]" or level == "[CRITICAL]":
                    time_date = f"{words[0]} {words[1]}"
                    self.time_stamps.append(time_date)

                    message = " ".join(words[4:])  # take the words after the 4th index as a 1 word
                    self.error_details.append((words[3], message))  # append using tuples

                if level not in self.log_counts:
                    self.log_counts[level] = 1  # if it doesn't exist
                else:
                    self.log_counts[level] += 1  # if it exists add 1

        print(self.log_counts)

        print("\n-- ERROR TIMESTAMPS --")
        for timestamp in self.time_stamps:
            print(timestamp)

        print("\n-- DETAILED ERRORS LOG --")
        for component, msg in self.error_details:  #component = error place,  msg = detailed error message
            print(f"[{component}] -> {msg}")  # outputs : error place -> error message

parser = LogParser("app.log")  # instantiate the object.. creates an empty self.log_counts dictionary
parser.parse_logs()  #call the method 

print("\n-------------------------------------------------------------")