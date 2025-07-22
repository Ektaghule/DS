#We use control transfer conditions and functions to determine the flow of execution in a program.
#This includes conditional statements, loops, and function calls. It consists of break, continue, return, and pass statements.
#Example of break statement
for i in range(10):
    print(i)
    if i == 5:
        break
    
count = 0
while True:
    print("Inside the loop")
    count += 1
    if count == 5:
        break 

#Example of continue statement
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for j in num:
    if j % 2 == 0:
        continue
    print(j)
    
i = 1
while i < 3:
    j = 0
    while j < 5:
        j = j + 1
        if j == 3:
            continue
        print(j)
    i = i + 1
    
#Exmple of pass statement
count = 0
while count < 5:
    pass  # It's just a placeholder, does nothing
    print(count)
    count = count + 1
    
#Functions: It is a reusable block of code that performs a specific task for a repetative times.

#Function definition
def greet(name):
    """Function to greet a person"""
    print(f"Hello, {name}!")
    
#Function calling
greet("Ekta")

def fruits_func(*fruits):
    """Function to print fruits"""
    print("Fruits is:"+ fruits[3])
fruits_func("Apple", "Banana", "Cherry", "Date")

def country(India):
    """Function to print country name"""
    print("Country is: " + India)
country("USA")
country("Canada")

#Task: Create a function "calc" in which it has to add, subtract, multiply and divide two numbers.
def calc(n1,n2):
    def add():
        return n1 + n2
    def sub():
        return n1 - n2
    def mul():
        return n1 * n2
    def div():
        return n1 / n2
    print(f"Add: {add()}")
    print(f"Sub: {sub()}")
    print(f"Mul: {mul()}")
    print(f"Div: {div()}")
calc(10,5)

#print() and return statement
#In Python, the print() function is used to output data to the console, while the return statement is used to 
# extract a value from a function and send it back to the caller.
def add_print(a, b):
    """Function to add two numbers"""
    print(f"Sum of numbers is: ",a+b)
    
def add_return(a, b):
    """Function to add two numbers and return the result"""
    return a + b

add_print(10, 20)
result = add_return(10, 20)
print(f"Result of addition is:", result)

#Armstrong number
#An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
def is_armstrong(num):
    """Function to check if a number is an Armstrong number"""
    print(f"Enter a number: ")
    num = int(input())
    sum = 0
    order = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(True)
    else:
        print(False)
is_armstrong(153)

def add_and_sub(a, b):
    """Function to add and subtract two numbers"""
    add_result = a + b
    sub_result = a - b
    return add_result, sub_result
result_add, result_sub = add_and_sub(10, 5)
print(f"Addition Result: {result_add}, Subtraction Result: {result_sub}")

#Nested functions
def outer_function(x):
    """Outer function that contains a nested function"""
    def inner_function(y):
        """Inner function that adds x and y"""
        return x + y
    return inner_function
result = outer_function(10)(5)
print(f"Result of nested function: {result}")

#*args and **kwargs
#*args and **kwargs are used in function definitions to allow for variable numbers of arguments.
#*args allows for any number of positional arguments, while **kwargs allows for any number of keyword arguments.
def variable_args(*args):
    """Function that takes variable positional arguments"""
    for arg in args:
        print(arg)
def variable_kwargs(**kwargs):
    """Function that takes variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
variable_args(1, 2, 3, 4)
variable_kwargs(name="Alice", age=30, city="New York")