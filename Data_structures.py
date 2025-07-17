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