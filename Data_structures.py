# Data structure is a way to store and organize data in an efficient manner.
# Types: 
# 1. List: Ordered collection of items, mutable, allows duplicates.
# 2. Tuple: Ordered collection of items, immutable, allows duplicates.
# 3. Sets: Unordered collection of unique items, mutable, no duplicates.
# 4. Dictionaries: Collection of key-value pairs, mutable, keys are unique.

#Creating lists
list1 = [] #Empty list
list2 = [1, 2, 3, 4, 5] #List with integers
list3 = ["apple", "banana", "cherry"] #List with strings
list4 = [1, "apple", 3.14, True] #List with mixed data types
#To identify the type of a list, we can use the type() function
print(type(list1))  
#Nested lists
list5 = [[1, 2, 3], ["apple", "banana"], [True, False]] #List containing other lists
#Accessing elements in a list
print(list2[1])  #Accessing the first element (index 1)
print(list5[0][1]) #Accessing the second element of the first nested list

#Sclicing lists
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[-4:-1])

my_list = [10, 20, 30, 40, 50, True, False]
max_element = max(my_list)  # Finding the maximum element
print(max_element)
min_element = min(my_list)  # Finding the minimum element
print(min_element)
sum_elements = sum(my_list)  # Summing the elements
print(sum_elements)

strings = ["apple", "banana", "cherry"]
max_string = max(strings)  # Finding the maximum string (alphabetically)
min_string = min(strings)  # Finding the minimum string (alphabetically)
print(max_element)
print(min_element)

#Repeat/Replecate elements in a list
repeated_list = [1, 2, 3] * 3  # Repeating the list three times
print(repeated_list)

#Inbuilt functions for lists
list6 = [1, 2, 3, 4, 5]
list6.append(6)  # Adding an element to the end of the list
print(list6)
list6.remove(3)  # Removing an element from the list
print(list6)
list6.extend([7, 8])  # Extending the list with another list
print(list6)
list6.insert(0, 0)  # Inserting an element at the beginning of the list insert(index,data)
print(list6)

#Comparision of lists
list7 = [1, 2, 3]
list8 = [1, 2, 3]
print(list7 == list8)  # True, because the elements are the same
list9 = [1, 2, 3]
list10 = [4, 5, 6]
print(list9 == list10)  # False, because the elements are different
print(list7 != list8)  # False, because the elements are the same
print(list9 != list10)  # True, because the elements are different
print(list7 < list8)  # False, because the lists are equal
print(list9 < list10)  # True, because the first list has smaller elements 
print(list7 > list8)  # False, because the lists are equal
print(list9 > list10)  # False, because the first list has smaller elements

#pop() method
list11 = [1, 2, 3, 4, 5]
popped_element = list11.pop()  # Removes and returns the last element
print(popped_element)  # Output: 5
popped_element_index = list11.pop(1)  # Removes and returns the element at index 1
print(popped_element_index)  # Output: 2

#del Statement
list12 = [1, 2, 3, 4, 5]
del list12[2]  # Deletes the element at index 2
print(list12)  # Output: [1, 2, 4, 5]

#clear() method
list13 = [1, 2, 3, 4, 5]
list13.clear()  # Removes all elements from the list
print(list13)  # Output: []

#Sorting lists
list14 = [5, 2, 9, 1, 5, 6]
list14.sort()  # Sorts the list in ascending order 
print(list14)  # Output: [1, 2, 5, 5, 6, 9]
list15 = ["banana", "apple", "cherry"]
list15.sort()  # Sorts the list of strings in alphabetical order
print(list15)  # Output: ['apple', 'banana', 'cherry']
#Sorting in reverse order
list16 = [5, 2, 9, 1, 5, 6]
list16.sort(reverse=True)  # Sorts the list in descending order
print(list16)  # Output: [9, 6, 5, 5, 2, 1]
#Sorting with a custom key
list17 = ["banana", "apple", "cherry"]
list17.sort(key=len)  # Sorts the list by the length of the strings
print(list17)  # Output: ['apple', 'banana', 'cherry']
#Reversing lists
list18 = [1, 2, 3, 4, 5]   
list18.reverse()  # Reverses the order of the list
print(list18)  # Output: [5, 4, 3, 2, 1]

#count() method
list19 = [1, 2, 3, 1, 2, 1]
count_of_1 = list19.count(1)  # Counts the occurrences of 1
print(count_of_1)  # Output: 3
index = list19.index(2)  # Finds the index of the first occurrence of 2
print(index)  # Output: 1
words = ["Hello", "world", "Hello"]
result = "".join(words)  # Joins the list of strings into a single string
print(result)  # Output: "Hello world Hello"

#Tuples
#Creating tuples
tuple1 = ()  # Empty tuple
tuple2 = (1, 2, 3, 4, 5) # Tuple with integers
tuple3 = ("apple", "banana", "cherry")  # Tuple with strings   
tuple4 = (1, "apple", 3.14, True)  # Tuple with mixed data types
#To identify the type of a tuple, we can use the type() function
print(type(tuple1))
#Nested tuples
tuple5 = ((1, 2, 3), ("apple", "banana"), (True, False))  # Tuple containing other tuples
#Accessing elements in a tuple
print(tuple2[1])  # Accessing the first element (index 1)
print(tuple5[0][1])  # Accessing the second element of the first nested tuple

#minimum maximum elements in a tuple
tuple6 = (10, 20, 30, 40, 50)  
max_element_tuple = max(tuple6)  # Finding the maximum element
print(max_element_tuple)  # Output: 50
min_element_tuple = min(tuple6)  # Finding the minimum element
print(min_element_tuple)  # Output: 10

#Sum of elements in a tuple
sum_elements_tuple = sum(tuple6)  # Summing the elements   
print(sum_elements_tuple)  # Output: 150

#converting a tuple to a list
tuple7 = (1, 2, 3, 4, 5)
list_from_tuple = list(tuple7)  # Converting tuple to list
print(list_from_tuple)  # Output: [1, 2, 3, 4, 5]

#count method in tuples
tuple8 = (1, 2, 3, 1, 2, 1)
count_of_1_tuple = tuple8.count(1)  # Counts the occurrences of 1
print(count_of_1_tuple)  # Output: 3

tuple9 = (1, 2, 3, 4, 5)
a, b, c, d, e = tuple9  # Unpacking the tuple into variables
print(a, b, c, d, e)  # Output: 1 2 3 4 5
tuple10 = (1, 2, 3, 4, 5)
a, *b, c = tuple10  # Unpacking with asterisk to collect remaining elements
print(a, b, c)  # Output: 1 [2, 3, 4] 5

combined_tuple = tuple9 + tuple10  # Concatenating two tuples
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)


#Sets - used when unique collection of items is needed
# It is muatble, unordered, uniindexed, and does not allow duplicates.
set1 = set()  # Empty set
set2 = {1, 2, 3, 4, 5}  # Set with integers
set3 = {"apple", "banana", "cherry"}  # Set with strings 
set4 = {1, "apple", 3.14, True}  # Set with mixed data types
# To identify the type of a set, we can use the type() function
print(type(set1))  # Output: <class 'set'>

#converting a list to a set
from_list = [1, 2, 3, 4, 5, 1, 2, 3]
to_set= set(from_list)  # Converting list to set
print(to_set)  # Output: {1, 2, 3, 4, 5} (duplicates removed)

print("cherry" in set3)  # Checking if an element is in the set
print("orange" in set3)  # Checking if an element is not in the set

len_set = len(set2)  # Finding the length of the set
print(len_set)  # Output: 5

set2.add(6)  # Adding an element to the set
print(set2)  # Output: {1, 2, 3, 4, 5, 6}

min_set = min(set2)  # Finding the minimum element in the set
print(min_set)  # Output: 1
max_set = max(set2)  # Finding the maximum element in the set
print(max_set)  # Output: 6

#Joint sets
set5 = {1, 2, 3}   
set6 = {3, 4, 5}
set_union = set5.union(set6)  # Union of two sets
print(set_union)  # Output: {1, 2, 3, 4, 5}
set_intersection = set5.intersection(set6)  # Intersection of two sets
print(set_intersection)  # Output: {3}
set_difference = set5.difference(set6)  # Difference of two sets
print(set_difference)  # Output: {1, 2}
set_symmetric_difference = set5.symmetric_difference(set6)  # Symmetric difference of two sets
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}

#update method
set7 = {1, 2, 3}
set8 = {4, 5, 6}
set7.update(set8)  # Updating set7 with elements from set8
print(set7)  # Output: {1, 2, 3, 4, 5, 6}
difference_update = set7.difference_update(set8)  # Updating set7 to remove elements in set8
print(set7)  # Output: {1, 2, 3}
intersection_update = set7.intersection_update(set8)  # Updating set7 to keep only elements in both sets
print(set7)  # Output: set() (empty set, as there are no common elements)

#Fun Task: Merge the below two tuples  and then remove the duplications and return the final output as a tuple
tup1= (1, 2, 3)
tup2= (3, 4, 5)
from_set1 = set(tup1)  # Converting a tuple to a set
from_set2 = set(tup2)  # Converting another tuple to a set
merge_set = set(from_set1).union(set(from_set2))  # Merging two sets into a set
to_tuple = tuple(merge_set)  # Converting the merged set back to a tuple
print(to_tuple)  # Output: (1, 2, 3, 4, 5) (duplicates removed)

#function definition
def merge_and_remove_duplicates(tup1, tup2):
    return set(tup1).union(set(tup2))  # Merging two tuples into a set to remove duplicates
    #funtion calling
    print(merge_and_remove_duplicates(tup1, tup2))  # Output: (1, 2, 3, 4, 5)
    

#Dictionaries - used to store data in key-value pairs {key:value}.
# It is mutable, unordered, and allows unique keys.
dict1 = {}  # Empty dictionary
dict2 = {"name": "Ekta", "age": 21, "city": "Pune"}  # Dictionary with key-value pairs
print(dict2) # Output: {'name': 'Ekta', 'age': 21, 'city': 'Pune'}
print(dict2['city'])  # Accessing the value associated with the key 'city'
dict2["country"] = "India"  # Adding a new key-value pair
print(dict2)  # Output: {'name': 'Ekta', 'age': 21, 'city': 'Pune', 'country': 'India'}
dict3 = {1: "apple", 2: "banana", 3: "cherry"}  # Dictionary with integer keys
dict4 = {"name": "Yuthika", "age": 20, "is_student": True}  # Dictionary with mixed data types
# To identify the type of a dictionary, we can use the type() function

#built-in functions for dictionaries
print(type(dict1))  # Output: <class 'dict'>
print(dict4.keys())  # Getting all keys in the dictionary
print(dict3.values())  # Getting all values in the dictionary
print(dict2.items())  # Getting all key-value pairs in the dictionary

del dict4["age"]  # Deleting a key-value pair by key
print(dict4)  # Output: {'name': 'Yuthika', 'is_student': True}

#Fun Task: Check if all the elements in the list are unique or not
list_unique = [1, 2, 3, 4, 2]
def are_elements_unique(lst):
    return len(lst) == len(set(lst))  # Compare length of list with length of set (which removes duplicates)
    print(are_elements_unique(list_unique))  # Output: False, because 2 is repeated
    
#Fun Task: Count of occurence of each element in the list
lst1=["a","b","a","b","c","a"]
def count_occurrences(lst):
    return {item: lst.count(item) for item in set(lst)}  # Create a dictionary with counts of each unique item
    print(count_occurrences(lst1))  # Output: {'a': 3, 'b': 2, 'c': 1}
    
#Fun Task: Swap the keys and values in the dictionary
dict5 = {"a": 1, "b": 2, "c": 3}
def swap_keys_values(d):
    return {value: key for key, value in d.items()}  # Create a new dictionary with keys and values swapped
    print(swap_keys_values(dict5))  # Output: {1: 'a', 2: 'b', 3: 'c'}
    
abc