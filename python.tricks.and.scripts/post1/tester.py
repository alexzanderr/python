
print('hello world!')

# calling the print_source_code function
from test import print_source_code
# test is my script where 
# i wrote the print_source_code function

# __file__ is a special 
# variable that contains
# the absolute path of 
# the current working python file
print_source_code(__file__)
print('end of the python_script.py')
