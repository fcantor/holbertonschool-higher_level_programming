#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{}".format(value))
        return True
    except Exception as err:
        print("Exception: {}".format(error), file=stderr)
        return False
