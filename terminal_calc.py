# @Date: August 2022

from lib2to3.pgen2 import token
from linked_list import *

# Will only work without user memory for now.
# Only works with whitespace considered.

print("\nWelcome to the terminal calculator.")
print("\nThis calculator only works with whitespace considered. eg. 1 + 1 returns 2; 1+1 errors.\n")
print('Enter HELP to view a list of commands.')
print('Enter EXIT to return to the terminal.\n')

def calculator():
        # Prompt input and tokenize.
        user_input = input('calc<<< ').lower()
        tokenized_input = user_input.split()
        lnk = make_lnk(tokenized_input) # Makes Linked List by mutating lnk.


        ###############
        ### COMPUTE ###
        ###############

        while lnk is not Link.empty: # This evaluates one line, then once finished calls calculator() for a new input.
            temp = lnk
            operators = ['/', '+', '-','*']

            ##############
            ### ERRORS ###
            ##############
            h, e = False, False # Boolean flags to determin error in calling HELP or EXIT.
            first_is_in = lnk.first in operators
            operator_error = 'print(\'OperatorError: Enter HELP to see a list of operators. Enter HELP: <operator> to view specific examples.\n\')'
            command_error = 'print(\'CommandError: You cannot call HELP and EXIT at the same time.\n\')'
            
            if first_is_in and lnk.rest is Link.empty: 
                eval(operator_error)
                break
            while temp is not Link.empty:
                if temp.first == 'help':
                    h = True
                if temp.first == 'exit':
                    e = True
                if e and h:
                    eval(command_error)
                    break
                temp = temp.rest
            first_helpc = lnk.first == 'help:'
            if first_helpc and (lnk.rest is Link.empty or lnk.rest.rest is not Link.empty):
                print('HelpError: \'help:\'<operator> must have an operator to the right of the colon.\n')
                break
            if first_helpc and lnk.rest.first not in operators:
                print('HelpError: The operator to the right of the colon must be a built-in operator. Enter HELP to view built-in operators.\n')
                break
            if lnk.first == '+' and not isinstance(eval(lnk.rest.first), int): # The case0 above already checks for if is empty
                print('OperatorError: The \'+\' operand is being used incorrectly. Call HELP to see how to use \'+\'.\n')
                break
        
            ########################
            ### CALLING COMMANDS ###
            ########################

            if lnk.first == 'exit':
                print('Bye! You are now in the terminal.\n')
                return
            if lnk.first == 'help':
                help()
            if lnk.first == 'help:':
                # call help_<operator>(), which gives examples of how to use operator.
                return
            #if lnk.first == '+':
             #   print('this is running')
            #   if lnk.rest.first == '-':
            #        print('-' + lnk.rest.rest.first)
            #    print(lnk.rest.first)
            
            if lnk.rest.first == '+':
                sum = eval(lnk.first + " + " + lnk.rest.rest.first)
                lnk = Link(sum, lnk.rest.rest.rest)
                print(sum)
                    

            #if isinstance(eval(lnk.first), int) and lnk.rest.first =='+': ## the above if with + and lnk.rest.rest evals as first
            #    sum = 0
            #    print(sum)
            #    while lnk is not Link.empty:
            #       sum += eval(lnk.first) + eval(lnk.rest.rest.first)
            #       print(sum, 'hi')
             #       lnk = lnk.rest.rest.rest.rest
            #    print(sum, 'hi')


            lnk = lnk.rest
        calculator()

     
def make_lnk(lst): # Only makes a new 'rest' if there exists a rest.
    lnk = Link(lst.pop(0))
    sub = lnk
    for a in lst:
        sub.rest = Link(a)
        sub = sub.rest
    return lnk


##########################
### BUILT-IN FUNCTIONS ###
##########################

def help():
    print("""
    '+'  --- the basic addition operator
    '-'  --- the basic negation operator (can be used to turn positive to negative)
    '/'  --- the basic division operator
    '*'  --- the basic multiplication operator
    '^'  --- the power operator (eg. 2^3 = 8)
    '()' --- the basic parenthesis of mathematical order of operations
    """)







######################################
### RUN THE CALCULATOR APPLICATION ###
######################################

calculator()
