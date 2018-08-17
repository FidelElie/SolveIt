from Libraries.ProblemManipulator import ProblemManipulator
from Libraries.DoMath import DoMath
from Libraries.FileHandler import FileHandler
import os 

def read_file():
    """Function to open the file to get the problem to be calculated"""
    open_file = FileHandler("r")  # calls the file handler class
    problem_string = open_file.mod_string()
    open_file.close_file()
    return problem_string

def manipulate_problem(problem_string):
    """Function that manipulates the lists of string to be used for the calculations"""
    math_problem = ProblemManipulator(problem_string) # calls problem manipulator class
    math_problem.check_operators()
    math_problem.ensure_single_ops()
    outputs = math_problem.prob_manip()
    return outputs[0], outputs[1], outputs[2]

def do_calculations(problem_numbers, problem_operators, op_start):
    """Function to do the main calculation"""
    do_the_math = DoMath(problem_numbers, problem_operators, op_start) # calls the do math class
    do_the_math.calculation()
    answer = do_the_math.answer()
    return answer

def write_file(answer):
    """Function to write answer back to file"""
    open_file_to_write = FileHandler("w") # calls the file handler class again in a different file mode
    open_file_to_write.write_answer(answer)
    open_file_to_write.close_file()

def main():
    """Main Running Function"""
    os.chdir(os.path.abspath("TextFiles"))
    # calls function to read the text file to get the problem
    problem_string = read_file() 
    # checks whether a problem was actually entered
    if len(problem_string) != 0:
        # calls function to sort and manipulate the problem so it can be calculated
        problem_numbers, problem_operators, op_start = manipulate_problem(problem_string)
        # calls function to calcualte the answer to the problem provided
        answer = do_calculations(problem_numbers, problem_operators, op_start)
        # calls function to write the calculated answer back to the file
        write_file(answer) 
    else: # if there wasn't one entered then the answer is set to error so that can be sent back
        answer = "Error"
        write_file(answer)
    # deletes the nul file created in the autohotkey script, so the while loop can be broken
    os.remove("Nulfile.txt") 
    os.chdir("..")
main()
