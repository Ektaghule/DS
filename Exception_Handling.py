#Types of errors in Python
# 1. SyntaxError: Raised when the parser encounters a syntax error.
# 2. LogicalError: Raised when the code is syntactically correct but produces an incorrect result.
# 3. RuntimeError: Raised when an error occurs during the execution of the program.
# 4. ImportError: Raised when an import statement fails to find the module definition.
# 5. ValueError: Raised when a function receives an argument of the right type but inappropriate value.
# 6. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 7. IndexError: Raised when a sequence subscript is out of range.
# 8. KeyError: Raised when a dictionary key is not found.
# 9. AttributeError: Raised when an invalid attribute reference is made.
# 10.NameError: Raised when a local or global name is not found.

#LogicalError Example
def divide_numbers(a, b):
    return a / b
# This will not raise an error, but it may produce an incorrect result if b is zero.

#RuntimeError Example
def divide_numbers_with_error(a, b):
    if b == 0:
        raise RuntimeError("Division by zero is not allowed.")
    return a / b

#Try block is the block which contains the code that may raise an exception.
#Except block is the block which contains the code that handles the exception.
try:
    result = divide_numbers_with_error(10, 0)
except RuntimeError as e:
    print(f"Runtime Error: {e}")

#Else block is the block which contains the code that will execute if no exception was raised in the try block.
# It is optional and can be used to execute code that should run only if the try block was successful.
#Finally block is the block which contains the code that will always execute, regardless of whether an exception was raised or not.
try:
    result = divide_numbers_with_error(10, 2)
except RuntimeError as e:
    print(f"Runtime Error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
    
#Task: User wants to access the index number 10 of a list that has only 5 elements.
my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[10])
except IndexError as e:
    print(f"Index Error: {e}")
else:
    print("Accessed index successfully.")
finally:
    print("Finished trying to access the list index.")
    
#Raise keyword is used to raise an exception manually.
def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive.")
    return num

try:
    print(check_positive_number(-5))
except ValueError as e:
    print(f"Value Error: {e}")
