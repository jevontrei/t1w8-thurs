import os
os.system("clear")

# [can we call a function that is defined below the call?]
def function_a():
    print("Function A started")
    function_b()
    print("Function A ended")


def function_b():
    print("Function B started")
    function_c()
    print("Function B ended")


def function_c():
    print("Function C started")
    # Intentional error:
    # result = 10 / 0
    # Debug it:
    result = 10 / 1
    print("Function C ended")


# Call the initial function
function_a()
