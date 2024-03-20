#new python file 

"""
#Date: 03/03/2024
# First
print("Hello, World!")

#indentation
if 5>2:
    print("You are right, five is greater than two.")
     
# four is common, && they have to be in the same line


#variable 
#they are created when you assign a value
x=5
y="Hello, hello beautiful people!!"

print(x)
print(y)
#variable type can be changed easily by just chaging the value
#so 
x=y
print(x)


#comments
#it doesn't have a multi line comments but instead useing triple unassigned string like three quotes 
#and that block gets ignored.



#Date: 03/04/2024

#casting variables assigns type to the data

x = str("Hello")
print(x)

#finding datatype of the value
print(type(x))

#double and single quotes are same
#variable names case sensitive
#follow basic rules of variable name

#assign multiple values in one line

x,y,z= "Hi",2,3.0
print(x)
print(y)
print(z)

x=y=z="Bitch"
print(x)
print(y)
print(z)



#this is like arrays but not really;[ it is called list]
fruits = ["apple", "banana", "cherry"]
x, y, z  = fruits
print(x)
print(y)
print(z)

#if i just leave out z, it isn't working 

#anyway you can even do this
#but it prints in one line

print(x,y,z)

#little change
#can even do 

print(x+y+z)



#Function

#if x is outside function it is global variable

x="Tea"

def myFunc():
  x="Coffee"
  print(x)

myFunc()
print(x)

#defining a variable global even inside the function makes it global for rest of the code
        

#Data Types

#weird data types
# 1. tupes .. we will get into it
# 2. range ... its like a sequence of numbers as in range(start, endBefore, step)
# 3. dict ... as in dictionary
x={"Name":"Parth", "Age":25}
print(x)

# 4. set.. idk we will get into it
# 5. frozenset ...idk
# 6. bytes
# 7. bytearray ...:(
  
#Remember: 
  
#  Tupes have ()
# list have []
#  set have {}
  


#Date: 03/13/24

#Numbers

#types of number 
# int
# float
# complex

#you can even convert them to each other
#except from complex to any number
#so if x = 5
# y = float(x) changes it to floating point #


#random number

import random

print(random.randrange(1,100,2))

#or

print(random.randrange(5))




#Casting
# assigning data types to variable.
# you would put x = int(2.3) return 2
# x = int(2) ..return 2
# x = int("2").. return 2 yes str to int
# but the str has to be int


#Strings

# "Hi" and 'Hi' are same
# so a string is an array of letters
# is a = "Hello, World"
# a[1] is e 

#len() prints length

# in function checks if the phrase is in the text 
# txt = "The best things in life are free!"
# print("free" in txt).... returns true 


#txt = "The best things in life are free!"
#if "free" in txt:
#  print("Yes, 'free' is present.")
# returns message....so we can use "in" in a "if statement"

#there is also a "not in"

#string slicing
# so if, a is 
a = "Hello, World"
print(a[0:4])  #prints Hell...so starts with H and ends with o BUT it doesn't include 0
print(a[-6:-1]) 
#prints " Worl"...so starts from back with "," and doesn't include "," but
#ends with l BUT also includes l



# Date: 03/17/2024

# String(cont.)

a = " This is a text lmao  "

# upper() will make upper case
# built in method

print(a.upper())

# lower() will make lower case
# built in method

print(a.lower())

# strip() will remove white space before and after the phrase
# built in method

print(a.strip())

# replace() replaces letters of our choice

print(a.replace("T","p"))

# splits() splits into substring

print(a.split("a"))
#the output would be:
#[' This is ', ' text lm', 'o  ']


#Date: 03/19/2024

#     String Concatenation

# which means combining two strings
a = "Hello,"
b = "Bitch"
c = a + " "+ b
print(c)

#           String Format
# The format() method takes the passed arguments, 
# formats them, and places them in the string 
# where the placeholders {} are:
# check out the example with the indexing

quantity = 4
itemNum = 32456
price = 6.75

myOrder = "I want to pay {2} dollars for {0} pieces of item number {1}"
print(myOrder.format(quantity,itemNum,price))

"""

