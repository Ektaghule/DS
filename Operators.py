x=2
y=10

#Arithmetic operators
print(x+y) #addition
print(x/y) #division
print(x-y) #substraction
print(x*y) #multiplication
print(x // y) #floor division
print(x ** y) #exponentiation
print(x % y) #modulus (remainder)

#Comparison operators
print(x == y) #equal to
print(x != y) #not equal to
print(x > y) #greater than
print(x < y) #less than
print(x >= y) #greater than or equal to
print(x <= y) #less than or equal to

#Logical operators
print(x > 0 and y > 0) #and
print(x > 0 or y < 0) #or
print(not(x > 0)) #not

#Identity operators
print(x is y) #is
print(x is not y) #is not

#Membership operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) #in
print(6 not in my_list) #not in
print('E' in 'Ekta')
print('k' not in 'Ekta')

#Bitwise operators
print(x & y) #bitwise AND
print(x|y) #OR
print(~x) #NOT
print(x<<1) #Left shift
print(y>>1) #Right shift
print(x^y) #XOR

#Assignment operators
x+=y  #x=x+y
print(x)
x-=y #x=x-y
print(x)
x%=y #x=x%y
print(x)
x/=y #x=x/y
print(x)
x*=y #x=x*y
print(x)