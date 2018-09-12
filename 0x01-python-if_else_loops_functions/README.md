# 0x01. Python - if/else, loops, functions

This project introduces the concepts of the if/else condition, loops, and functions in the Python programming language. All tasks are Python scripts, except the last one, which is a C function and header, and is written as a technical interview prep. The importing of modules are not allowed for each task.

---

## 0. Positive anything is better than negative nothing
file: ```0-positive_or_negative.py```

This Python program will assign a random signed number to the variable ```number``` each time it is executed, will print out that number and whether it is positive or negative.

## 1. The last digit
file: ```1-last_digit.py```

This Python program will assign a random signed number to the variable ```number``` each time it is executed. It will then print out the number, its last digit, and whether it's:
- greater than 5
- is 0
- is less than 6 and not 0

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
file: ```2-print_alphabet.py```

This Python program prints the alphabet, in lowercase, using only loop, one print function with string format,  and not followed by a new line.

## 3. When I was having that alphabet soup, I never thought that it would pay off
file: ```3-print_alphabt.py```

This Python program prints the alphabet, in lowercase, except the letters ```q``` and ```e```. Only one print function and one loop are allowed. Characters can't be stored in a variable, and modules are not allowed to be imported.

## 4. Hexadecimal printing
file: ```4-print_hexa.py```

This Python program prints all numbers from 0 to 98 in decimal and in hexadecimal.

## 5. 00...99
file: ```5-print_comb2.py```

This Python program prints numbers from 0 to 99. Numbers are separated by ```,``` followed by a space. Numbers are printed in ascedning order with two digits, and the last number is followed by a new line. Only 2 ```print``` functions with string format are allowed, as well as one loop. Storing numbers or strings in a variable, as well as importing modules, are not allowed.

## 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
file: ```6-print_comb3.py```

This Python program prints all possible different combinations of two digits. Numbers are separated by ```,``` followed by a space. The two digits must be different, therefor numbers like ```01``` and ```10``` are considered the same combination of the digits ```0``` and ```1```. No more than 3 ```print``` functions with string format, as well as 2 loops, are allowed. Storing numbers or strings in a variable, as well as importi\
ng modules, are not allowed.

## 7. islower
file: ```7-islower.py```

This Python program checks for lowercase characters. Returns True if ```c``` is lowercase, otherwise it returns ```False```. Importing modules isn't allowed, as well as the use of the functions ```str.upper()``` and ```str.isupper()```.

## 8. To uppercase
file: ```8-uppercase.py```

This Python program prints a string in uppercase. Only one loop and 2 ```print``` functions with string format are allowed. Importing modules isn't allowed, as well as the u\
se of the functions ```str.upper()``` and ```str.isupper()```.

## 9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important
file: ```9-print_last_digit.py```

This Python function prints the last digit of a number. Importing modules isn't allowed.

## 10. a + b
file: ```10-add.py```

This Python function adds two integers and returns the result. Importing modules isn't allowed.

## 11. a ^ b
file: ```11-pow.py```

This Python function computes ```a``` to the power of ```b``` and returns the value. Importing modules isn't allowed.

## 12. Fizz Buzz
file: ```12-fizzbuzz.py```

This Python program prints the numbers from 1 to 11 separated by a space. For multiples of three, it  prints ```Fizz```, for multiples of five, it prints ```Buzz```, and for multiples of both three and five, it prints ```FizzBuzz``` instead of the number.

## 13. Insert in sorted linked list
file: ```13-insert_number.c, lists.h```

This C function inserts a number into a sorted singly linked list. It returns the address of the new node, or ```NULL``` if it failed.