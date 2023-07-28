# import packages
import sys # handles command line arguments, system calls
import os # interacts with operating system
import csv # reads csv file into memory

class Contact:
    def __init__(self, timestamp, name, email, org, sent):
        self.timestamp = timestamp
        self.name = name
        self.email = email
        self.org = org
        self.sent = sent
    
    def __str__(self):
        return (f"[{self.timestamp}, {self.name}, {self.email}, {self.org}, {'sent' if self.sent else 'not sent'}]")

def main():
    # get the path of the CSV file
    # sys.argv is a list of command line arguments
    # sys.argv[0] is the name of the program itself (mailbot.py)
    # sys.argv[1] will be the first argument after the program name
    # sys.argv[2] will be the second argument after the program name, etc
    # exit the program if no path to CSV file is provided
    if len(sys.argv) < 2:
        print("Missing path to CSV file\nUsage: python3 mailbot.py myfile.csv")
        # sys.exit(1) exits with an error
        # sys.exit(0) can be used to exit without an error
        sys.exit(1)
    # get the path to the CSV file from the command line argument
    path = sys.argv[1]
    # check if file exists
    if not os.path.exists(path):
        sys.exit("Error: File '{}' not found".format(path))
    if not os.path.isfile(path):
        sys.exit("Error: '{}' is not a file".format(path))
    # call open() to get contents of file (with read permissions)
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            c = Contact(r[0], r[1], r[2], r[3], sent=False)
            print(c)
    

# ref https://docs.python.org/3/reference/toplevel_components.html#complete-python-programs
# ref https://docs.python.org/3/reference/import.html?highlight=__name__#__name__
if __name__ == "__main__":
    main()
