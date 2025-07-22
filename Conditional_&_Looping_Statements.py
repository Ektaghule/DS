#conditional Statements and loops
#Example of an if statement
x = 5
if x > 0:
    print("x is positive")
    
# Example of an if-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#Task: Given a number, verify that the number is a multiple of 2 or not?
user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print(f"{user_input} is a multiple of 2")
else:
    print(f"{user_input} is not a multiple of 2")
    
#Take: In the given dictionary, check if the key 'name' exists or not?
my_dict = {'a':1,'b':2,'c':3}
key_to_check = 'b'
if 'b' in my_dict:
    print(f"Key 'b' exists in the dictionary")
else:
    print(f"Key 'b' does not exist in the dictionary")
    
# Example of a elif statement
x = 15
if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is between 10 and 20")

a=10
b=20
c=30
if a < b and b < c:
    print("a is less than b and b is less than c")
elif a > b and b > c:
    print("a is greater than b and b is greater than c")
elif a == b or b == c:
    print("Either a is equal to b or b is equal to c")
else:
    print("No conditions met")
    
#Nested conditional statements
x = 10
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
        
#Shorthand if statement
x = 5
print("x is positive") if x > 0 else print("x is not positive")

txt = "Hello World"
result = True if "Hello" in txt else False
print(result)

score = 85
result = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else'F'
print(f"Your grade is {result}")

#Task: Write a program to take three sides lenghts  and print weather the triangle is equilateral, isosceles or scalene
side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))
if side1 == side2 == side3:
    print("The triangle is equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("The triangle is scalene")
    
#Task: Write a program that prints "Fizz" if a number is divisible by 3, "Buzz" if it is divisible by 5, and "FizzBuzz" if it is 
# divisible by both, or the number itself otherwise.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#Write a program that checks if a given string is a palindrome or not.
input_string = input("Enter a string: ")
if input_string == input_string[::-1]:
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")

#Example of for loop
for i in range(5):
    print(i)
    
#Task: Write a program to print the first 10 even numbers
number = [1,2,3,4,5,6,7,8,9,10]
for i in number:
    if i % 2 == 0:
        print(i)
else:
    print("Number is not even")

#Print maximum even number in the list
number = [10,50,40,305,15]
max_even = None
for i in number:
    if i % 2 == 0:
        if max_even is None or i > max_even:
            max_even = i
if max_even is not None:
    print(f"The maximum even number in the list is {max_even}")

#List comprehension
#synatax: new_list = [expression for item in iterable]
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

#Generator expression
#syntax: new_gen = (expression for item in iterable)
gen_squares = (x**2 for x in range(10))
print("Squares of numbers from 0 to 9 using generator expression:")
for square in gen_squares:
    print(square)

#Nested for loop
for i in range(1,3):
    for j in range(1,6):
        print(i*j, end='\t')
    print()  # New line after each inner loop iteration

#Example of while loop
count = 0
while count < 5:
    print(count)
    count += 1

#Task: Find  the sum of all even numbers from  1 to 100 using a for loop
sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print(f"The sum of all even numbers from 1 to 100 is {sum_even}")

#Task : Write  a program to calulate the factorial of a number using a while loop
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial is {factorial}")
