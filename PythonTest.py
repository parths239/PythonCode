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




# Casting
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

#when you do split it becomes 

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

item = "ice tea"
time = 8
location = "made coffee"

theOgString = "Today I got {0} at {1} AM from {2}"
print(theOgString.format(item,time,location))

# Date: 03/21/2024

#  *** String Booleans **
# apart from basic comparisons we also have bool() func 
# that returns true or false 
# 
# ex1 
if 5>15:
  print("It is greater")
else:
  print("It is not")

print(bool(5>15))

bool("Hi") #has a value of true
print(bool(95)) #returns true
print(bool(0))  #returns false


# ** Operators ** 
# +, - , *, /,
# % modulus
# ** exponents 2**5 ..returns 32
# // floor division .. returns neartest whole no in division ans

# basic comparison operator
# but the new ones are: 

# "is" returns true if both variable are same
# like, x is y is true is x=y

# "is not" returns true if both variable are not same
# like, x is not y is true is x!=y

# then there is, in and not in

# now interesting
# print(6 & 3)
# returns 2


#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

#6 = 0000000000000110
#3 = 0000000000000011
#--------------------
#2 = 0000000000000010
#====================


# |	... OR	.....Sets each bit to 1 if one of two bits is 1 ..X | Y
# ^	... XOR ....Sets each bit to 1 if only one of two bits is 1.. X ^ Y
# check more out at: https://www.w3schools.com/python/python_operators.asp

#The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

#If you push 00 in from the left:
# 3 = 0000000000000011
#becomes
#12 = 0000000000001100


# and >> moves the zeros to right


# Date: 03/23/2024

#*************************************************************************************************
# 
#    1. List is a collection which is ordered and
#        []                          changeable. 
#                                     Allows duplicate members.
#
#    2.Tuple is a collection which is ordered and 
#        ()                           unchangeable. 
#                                     Allows duplicate members.
#
#   3. Set is a collection which is   unordered, 
#      {}                             unchangeable*, and unindexed. 
#                                      No duplicate members.
#
# [ *Set items are unchangeable, but you can remove and/or add items whenever you like.]
#
#
#   4. Dictionary is a collection which is ordered** and x2
#                                          changeable. 
#                                          No duplicate members.
#
#***********************************************************************************************

# *** LISTS ***

# list uses []
# Its like an array
# List items are ordered, changeable, and allow duplicate values. 
# They uses index for location
# If you add new items to a list, the new items will be placed at the end of the list. 
# an example here:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # prints the exact list
print(len(thislist)) # prints length
list1 = ["abc", 34, True, 40, "male"] # list could have any data type
print(type(list1)) # so lists is itself a data type

# another way to make a list is

anotherList =  list(("Hi","This", "Iz","another","List", 4, "u"))

# notice how we use curved brackets make list with list function

#this would print banana
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#prints cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# prints the range of values so it would start at cherry and end at kiwi 
# but won't include melon @ 5

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# this would start at 0 and end at orange 

print(thislist[2:])
# this starts at cherry to end

print(thislist[-4:-1])
# negative indexing means u get "orange", "kiwi", "melon"

if "apple" in thislist: # checks if sth is in the list
  print("true")



# Date: 03/27/2024
  
# to add item to the list you can just relace at specific index 
# or change it by a range 

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# thislist[1] = "watermelon"
# print(thislist) --> watermelon instead of banana

# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist) --> this would change from 1 & 2 's value


#  Insert method in lists

#  thislist = ["apple", "banana", "cherry"]
#  thislist.insert(2, "watermelon")
#  print(thislist)

# Append method adds item at the end
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# extend method add another lists/sets/dic/whatever to the OG list
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#remove method
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist) -> remove first banada found

# pop method
# thislist.pop(1) -> removes from index 1
# thislist.pop() -> removes last element

# del keyword
# del thisList[1] -> removes value at 1
# del thisList -> deletes the whole list

# clear method
# thislist.clear() -> empties the list but list exists


# *** Looping in Lists ***

#for loops
thisList = ["Pen", "Notebook", "wallet", "keys"]
for x in thisList:
  print(x)
  
thisList = ["Pen", "Notebook", "wallet", "keys"]
for x in range(len(thisList)):
  print(thisList[x])
 
# while loop

thisList = ["Pen", "Notebook", "wallet", "keys"]
i = 0
while i < len(thisList):
  print(thisList[i])
  i = i+1
  
  
#*** List compression ***

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Normal code example
 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#  newlist = []
#  for x in fruits:
#     if "a" in x:
#     newlist.append(x)
#  print(newlist)

# Same Code can be written as
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#****************** LIST COMPRESSION FORMULA **********************
#
# newlist = [ expression for item in iterable if condition == True]
# 
# 
# The return value is a new list, leaving the old list unchanged.
# The condition is optional and can be omitted
# iterable can be any iterable object, like a list, tuple, set 
# we can also use range() for iterable
# 
#******************************************************************

# another example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# for the part, x if x != "banana" else "orange" , 
# it keeps x from fruits is x is not banana 
# but if it is banana it changes to orange



#** Sorting in Lists ***#

thislist.sort() #would sort alphabetically or numerically

thislist.sort(reverse = True) # sorted in a descending order

thislist.sort(key = str.lower) # sorting is case sensitive 
# so all capital letters being sorted before lower case letters 
# therefore we use all str to lower but OG value doesnt change

#custom sorting
thislist= ["some", "content"]
def myfunc(n):
    return #some property or equation# ** 
thislist.sort(key = myfunc) # using key = function to sort
print(thislist) 

# reverses the order of list but not sorting
thislist.reverse()


##**** copying lists ***###
list1 = []
list2 = list1 # won't work because it would the same list with different names

# but

list2 = list1.copy() # would make new list and changes to list2 wont change list1

# you can also do

list2 = list(list1)
#usingn the list function



#**** JOINING LISTS ****#
#
# method 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# method 2
# append to second list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#method3
# extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
#extending list1 by adding list2


#*** Other methods

#count()
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")

#index() returns where sth is located
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

"""

# Date: 04/02/24


##******** TUPLE **********
# I'd say read the W3school page
# simple thing: for tuple with one element just put comma after first element

thisTuple = ("Hello",)

# you can't edit the tuple but you can convert it to list, change the list, 
# and turn it back into tuple

thisTuple=("Hello", "World")
thisList = list(thisTuple)
thisList[1] = "Parth"
thisTuple = tuple(thisList)

print(thisTuple)

# Unpacking: allows assigning values from tuple to variable

# Please read here: https://www.w3schools.com/python/python_tuples_unpack.asp

# multiple tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 
# prints ("apple", "banana", "cherry", "apple", "banana", "cherry")

## Tuple methods:

# count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x) 

# index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x) #returns 3

