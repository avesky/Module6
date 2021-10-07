"""
Program: validate_input_in_functions.py
Author: Andy Volesky
Last date modified: 10/06/2021

The purpose of this program:

Write a function score_input() that takes parameters test_name, test_score, and invalid_message that validates
the test_score, then returns a string.

Open project Module6 with directory more_functions. Add file validate_input_in_functions.py.

Write the function with the following requirements:

The test_name is a mandatory parameter and will not need validation.
The test_score is optional, with default value that is negative, eg -1, and will be validated to be between 0-100
The invalid_message is optional, with default value 'Invalid test score!'

In the function add appropriate code to validate the the parameter value for test_score.
You may need to cast the input from string to the appropriate numeric type.

Return the string with test name and score if it passes validation; otherwise return the test name with invalid_message.

Write in the main() calls that demonstrate the following, the first one includes an example:

one good input:
display_string = score_input('Test 1', 70)  # function call, store in a variable
print(display_string)  # print the result of the function
one value below range
one value above range
one non-numeric input (make sure you account for an exception!)
"""

def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    try:
        if 0 <= test_score <= 100:
            return f"{test_name}: {test_score}"
        elif test_score < 0 or test_score > 100:
            return invalid_message
    except:
        print('Numbers only please')

if __name__ == '__main__':
    display_string = score_input('Test 1', 60)  # function call, store in a variable
    print(display_string)  # print the result of the function
    display_string = score_input('Test 2', -8)  # function call, store in a variable
    print(display_string)  # print the result of the function
    display_string = score_input('Test 3', 105)  # function call, store in a variable
    print(display_string)  # print the result of the function
    display_string = score_input('Test 4', 'asdf')  # function call, store in a variable
    print(display_string)  # print the result of the function