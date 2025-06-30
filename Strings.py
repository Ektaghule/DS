#Comparison of strings
string1 = "orange"
string2 = "kiwi"

print(string1 == string2) #Equal to
print(string1 <= string2) #Less than equal to
print(string1 >= string2) #Greater than equal to
print(string1 < string2) #Less than
print(string1 > string2) #Greater than
print(string1 != string2) #Not equal to


#ord function is used to get the ascii code of the characters
ord("e")

#Replace function
og_string = "Hey Ekta!"
new_string = og_string.replace("Hey","Hello")
print(new_string)

#Split function
sentence = "It's good weather outside"
word = sentence.split(" ")
print(word)
sentence2 = "Nice to meet you!"
word2 = sentence2.split(".")
print(word2)

#Formatting
date = 13
s1 = f"Hi, today's date is {date}"
print(s1)

#Strip function -> removes the white spaces from the begining and the end
s2="     Good evening"
print(s2.strip())

#Index function -> returns the index number of the specified string
s3="Ola it's me!"
index=s3.index("it's")
print(index)
index2 =s3.index("Hey")
print(index2)

#find function -> finds the string and returns the index number of it (The difference b/w index and find function is index gives 
# error when the substring is not in the string and find function return -1 when the substring is not in the string)
s3="Ola it's me!"
find=s3.find("it's")
print(find)
find2 =s3.find("Hey")
print(find2)

s1="Welcome"
s2="Welcome123"
print(s1.isalpha())
print(s2.isalpha())

#count() -> returns how many time a character is there in the provided main string
s1="This is a string"
count=s1.count("a")
print(count)
s2="Riya loves to travel"
count2=s2.count("t")
print(count2)


s1="HELLO"
print(s1.isupper())

s2="HEllo"
print(s2.islower())

s3="abc123"
print(s3.isdigit())


s1="hello WORLD!"
