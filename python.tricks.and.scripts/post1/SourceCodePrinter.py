
# for example
# on windows: pyabsolute_path == 'D:\\python_script.py'
# on linux: pyabsolute_path == '/user/python_script.py'
# on mac: same as linux

def print_source_code(pyabsolute_path):
    print('Source Code for this file =>')
    print(pyabsolute_path)
    print('~' * 100) # these are for aesthetics
    # opening the file in 'read' mode with utf-8
    # utf-8: uniform transformation format with 8 bit
    with open(pyabsolute_path, 'r', encoding='utf-8') as python_file:
        # reading first line
        line = python_file.readline()
        # looping through the python file, it will stop when we encounter ''
        while line:
            print(line, end='')
            line = python_file.readline()
    print()
    print('~' * 100) # these are for aesthetics