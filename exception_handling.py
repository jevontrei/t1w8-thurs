import os
os.system("clear")


def convert_to_integer(value):
    # print(type(value))
    try:
        result = int(value)
        print(f"Conversion successful! Result: {result}")
    except ValueError:
        print("Coversion failed. Please enter a valid integer.")
    finally:
        print("Closing any open resources.")


# User input
user_input = input("Enter a number to convert to integer: ")

# Convert the number
convert_to_integer(user_input)

# [error: becuase int() can't convert a float-like string to int ?!]
