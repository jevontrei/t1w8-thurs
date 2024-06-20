# t1w8-thurs

# 4 Pillars of OOP (contd..)

- Banking System

# repr method

- \_\_repr\_\_
- Special method, like \_\_init\_\_, which is used to define a string representation
- Particularly used for debugging and development because it can give detailed info about an object

# Composition of OOP

- Design principle where a class is composed of one or more objects from other classes
- It's an alternative to Inheritance and is often more flexible and modular
- Avodis inheritance's pitfall: Changes in the base class can unintentionally affect the derived class, which may break their functionality
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interfaces

# Error Handling

## Taxonomy of Python Errors

- Silent logical errors:
  - Code that runs fine, but is logically incorrect
  -
- Assertion errors:
  - raised when "assert" statement fails
  - if condition is True, nothing happens; if False, raises AssertionError
  -
- Syntax errors:
  - Errors in the written syntax that the Python interpreter cannot understand
  -
- Exceptions:
  - Runtime errors, occurs during program execution. Python has built-in exception to handle common errors
  - [also called runtime errors?]
  - Attribute Errors
  - OS Errors
  - User-defined exceptions
  - [see errors.py for more error types]
  - [Exception is a class?]
  -
- [to test code is running properly, print as much as you can! every step of the way]

# Stack Trace Interpretation

- Text that appears when Python encounters an exception, "stack trace"
- When exception occurs, the interpreter prints a stack trace that shows where the error happened and how the code reached that point
- Start with: Exception, then the trace

# Try / Except / Finally

- Comprehensive way to handle exceptions
- Ensures code always runs, regardless whether an error occurs
- "try" block has code that may raise exception
- "except" block has code that handles exception
- "finally" block has the code that should always be executed
- finally block is optional 


[there are way more types of errors!]