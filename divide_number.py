import os
os.system("clear")


def divide_numbers():
    try:
        # Get user input
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform division
        result = dividend / divisor
        print(f"Result of division: {result}")

    # except ZeroDivisionError:
    #     print("Error! Division by zero is not allowed.")
    # except ValueError:
    #     print("Error! Please enter valid numbers.")
    # to generalise for other error types [makes the above except blocks redundant, unless I want to add more personalised messages]:
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Division operation closed.")


# Perform division
divide_numbers()
