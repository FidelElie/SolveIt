import math

class DoMath(object):
    """Class that does the mathematics calculations"""
    def __init__(self, numbers, operators, op_position):
        self.numbers = numbers
        self.operators = operators
        self.op_position = op_position

    def float_convert(self):
        """Method that converts the numbers strings to floats"""
        for i in range(0, len(self.numbers)):
            self.numbers[i] = float(self.numbers[i]) # maps all numbers to their float value

    def check_first_op_position(self):
        """Method to check if the first position in the problem is an operation"""
        if self.op_position == True:   # operator was first in the calculation 
            mod_numb = float("{}{}".format(self.operators[0], self.numbers[0])) # add the operator to its number
            self.numbers[0] = mod_numb # modify the number
            del self.operators[0] # delete operator from list
        else:
            None

    def check_special_chars(self):
        """Method for taking into account special constants"""
        for i in range(0, len(self.numbers)):
            if self.numbers[i].lower() == "e":
                self.numbers[i] = math.e # converts e to its numerical value
            elif self.numbers[i].lower() == "pi":
                self.numbers[i] == math.pi # converts pi to its numerical value
            else:
                None

    def calculation(self):
        "Method loop used to calculate the problem"""
        self.check_special_chars()  # check for the constants
        self.float_convert()  # converts all the nunbers to floats 
        self.check_first_op_position() # - check method -
        while len(self.operators) != 0: # loops calculation method over the amount of operators
            self.idmas_procedure()

    def idmas_procedure(self):
        """Method that uses idmas order for calculations"""
        i = 0
        while i < len(self.operators): # checks indices
            if self.operators[i].lower() == "**" or self.operators[i] == "^":
               calculation = self.det_calc(self.numbers[i], self.numbers[i + 1], "ind")
               self.remapper(i, calculation)
               i += 1
            else:
                break
        i = 0
        while i < len(self.operators): # checks division
            if self.operators[i].lower() == "/":
               calculation = self.det_calc(self.numbers[i], self.numbers[i + 1], "div")
               self.remapper(i, calculation)
               i += 1
            else:
                break
        i = 0
        while i < len(self.operators): # checks multiplication 
            if self.operators[i].lower() == "x" or self.operators[i]=="*":
               calculation = self.det_calc(self.numbers[i], self.numbers[i + 1], "mult")
               self.remapper(i, calculation)
               i += 1
            else:
                break
        i = 0
        while i < len(self.operators): # checks addition 
            if self.operators[i].lower() == "+":
               calculation = self.det_calc(self.numbers[i], self.numbers[i + 1], "add")
               self.remapper(i, calculation)
               i += 1
            else:
                break
        i = 0
        while i < len(self.operators): # checks subtraction 
            if self.operators[i].lower() == "-":
               calculation = self.det_calc(self.numbers[i], self.numbers[i + 1], "sub")
               self.remapper(i, calculation)
               i += 1
            else:
                break
  
    def remapper(self, i, calculation):
        """Method used to modify the different lists for further calculations""" 
        del self.numbers[i +1]
        del self.numbers[i]
        del self.operators[i]
        self.numbers.insert(i, calculation) # replaces both values with the new calcualted value
     
    def answer(self):
        """Method to print final answer"""
        check_for_integer = self.numbers[0].is_integer()  # check if answer is an integer float 
        if check_for_integer == True:
            self.numbers[0] = int(self.numbers[0])  # make it an integer i.e get rid of the decimal place
        else:
            None
        return self.numbers[0]  

    def det_calc(self, A, B, operation_to_do):
        """Method to do the calculations between two of the numbers"""
        if operation_to_do == "add":  # adds two values
            sub_calc = A + B
        if operation_to_do == "sub":    # subtracts two values
            sub_calc = A - B
        if operation_to_do == "mult":  # multiplies two values
            sub_calc = A * B
        if operation_to_do == "div":  # divides two values
            sub_calc = A / B
        if operation_to_do == "ind": # puts one value to the power of the other
            sub_calc = A ** B
        return sub_calc
