import os

class FileHandler(object):
    """Class that handles reading and writing to file"""
    def __init__(self, mode):
        self.file_name = "ProblemAndAnswer.txt"
        self.mode = mode # defines what mode the file should be opened in
        self.file_object = open(self.file_name, self.mode)

    def mod_string(self):
        """Method used to read string from file and make it usable 
        byt the rest of the programme"""
        defined_string = self.file_object.read()
        defined_string = defined_string.split(" ") #gets rid of the spaces in between numbers and operators
        del defined_string[-1]  # deletes the "eq" that was used to show that the user was done entering the problem
        return defined_string

    def write_answer(self, answer):
        """Method to overwrite the file with the answer to the calculation"""
        self.file_object.write(str(answer)) # converts the answer to a string to be written to the file
    
    def close_file(self):
        """Method to close the file after use"""
        self.file_object.close()
        