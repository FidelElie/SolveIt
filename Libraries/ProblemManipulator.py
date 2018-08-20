class ProblemManipulator(object):
    """Class for doing the first manipulations of the problem object"""
    def __init__(self, problem):
        self.problem = problem
        self.numbers = []
        self.operations = []

    def check_operators(self):
        """Method for working out whether the signs should change e.g. 
        if there is a number subtracted from a negative - - becomes +"""
        for i in range(0, len(self.problem) - 1):
            if self.problem[i] == "-" and self.problem[i + 1] == "+": # a - and + become -
                del self.problem[i]
            elif self.problem[i] == "+" and self.problem[i + 1] == "-": # a + and - become -
                del self.problem[i]  
            elif self.problem[i] == "-" and self.problem[i + 1] == "-": # a - and - become + 
                del self.problem[i]
                self.problem[i+1] = "+"
            else:
                continue

    def ensure_single_ops(self):
        """Method to ensure that no two operations are next to eachother so
        they can be sorted into numbers and operators very easily"""
        for i in range(0, len(self.problem) - 1):
            if self.problem[i] == "*" and self.problem[i + 1] == "-": # checks if there is a multiply and subtract sign next to eachother
                mod_number = "{}{}".format(self.problem[i + 1], self.problem[i + 2])
                self.problem[i + 1] = mod_number
                del self.problem[i + 2]
            elif self.problem[i] == "x" and self.problem[i + 1] == "-": # alternate multuplication sign
                mod_number = "{}{}".format(self.problem[i + 1], self.problem[i + 2])
                self.problem[i + 1] = mod_number
                del self.problem[i + 2]
            elif self.problem[i] == "/" and self.problem[i + 1] == "-":  # checks if there is a division and subtract sign next to eachother
                mod_number = "{}{}".format(self.problem[i + 1], self.problem[i + 2])
                self.problem[i + 1] = mod_number
                del self.problem[i + 2]
            elif self.problem[i] == "^" and self.problem[i + 1] == "-": # checks if there is a indice next to the a subtract sign
                mod_number = "{}{}".format(self.problem[i + 1], self.problem[i + 2])
                self.problem[i + 1] = mod_number
                del self.problem[i+2]
            else:
                continue
                
    def prob_manip(self):
        """Method that sorts the problem into two different lists, one for the numbers
        and one for the operators to be used on them"""
        if self.problem[0] == "-" or self.problem[0] == "+":
            self.operations.append(self.problem[0])
            for i in range(1, len(self.problem), 2):
                self.numbers.append(self.problem[i])
            for i in range(2, len(self.problem), 2):
                self.operations.append(self.problem[i])
            op_postion = True # this determines whether an operator is first in the problem
        else:
            for i in range(0, len(self.problem), 2):
                self.numbers.append(self.problem[i])
            for i in range(1, len(self.problem), 2):
                self.operations.append(self.problem[i])
            op_postion = False  # false means that a number is first in the problem. 
        return self.numbers, self.operations, op_postion
