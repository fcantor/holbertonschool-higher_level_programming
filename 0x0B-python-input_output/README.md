# 0x0B. Python - Input/Output

## What you should learn from this project
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements for Python scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Requirements for Python test cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

---
File | Description
---|---
0-read_file.py | Function that reads a text file (UTF8) and prints to stdout
1-number_of_lines.py | Function that returns the number of lines of a text file
2-read_lines.py | Function that reads ```n``` lines of a text file (UTF8) and prints to stdout
3-write_file.py | Function that writes a string to a text file (UTF8) and returns the number of characters 
4-append_write.py | Function that appends a string at the end of a text file (UTF8) and returns the number of characters added
5-to_json_string.py | Function that returns the JSON representation of an object (string)
6-from_json_string.py | Function that returns an Object represented by a JSON string
7-save_to_json_file.py | Function that writes an Object to a text file, using JSON representation
8-load_from_json_file.py | Function that creates an Object from a "JSON file"
9-add_item.py | Script that adds all arguments to a list, and saves them to a file
10-class_to_json.py | Function that returns the dictionary description with simple data structure for JSON serialization of an object
11-student.py | Class that defines a student, and function that retrieves a dictionary representation of that class' instance
12-student.py | Same as
13-student.py | Same as
14-pascal_triangle.py | Function that returns a list of lists of integers representing the Pascal's triangle of n

## Author
Francesca Cantor