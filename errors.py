import os
os.system("clear")

# Silent errors


def is_even(number):
    return number % 2 == 1


# print(is_even(4))

print("-------------------")

# Assertion errors
# assert 2 + 2 == 5

print("-------------------")

# Syntax errors
# print("Hello world
# ^^ type of Exception error?

print("-------------------")

# Exceptions (runtime errors)
print("-------------------")

# Standard exception
# IndexError: raised when a sequence subscript is out of range
my_list = [1, 2, 3]
# print(my_list[3])

# KeyError: raised when a dict key is not found
my_dict = {
    "name": "Rachael"
}
# print(my_dict["age"])

# ValueError: raised when a fn receives an arg of the correct type but inappropriate value
# int("abc")

# TypeError: raised when an operation or fn is applied to an object of inappropriate type
# print(len(123))

print("-------------------")


# Attribute Errors: Raised when an attribute reference or assignment fails.

NoneType = None
# NoneType.abc

print("-------------------")

# ZeroDivisionError: raised when the second operand of a division or modulo operation is zero
# print(10/0)

# FileNotFoundError: raised when trying to open a file that does not exist
# open("random_file.txt")

print("-------------------")

# OS Errors: raised for system-related errors, like "disk full"

print("-------------------")

# User-defined exceptions: users create by subclassing the built-in Exception class


class myCustomError(Exception):
    pass


raise myCustomError("Hey mate! There is an error.")


print("-------------------")

# Stack Trace Interpretation

# math.pow(3)

from module_1 import function_A

function_A.execute()
