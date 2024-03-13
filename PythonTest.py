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
  
"""

#Date: 03/13/24

#Numbers

#types of number 
# int
# float
# complex

#you can even convert them to each other
#except from complex to any number

#random number

import random

print(random.randrange(1,100,2))

#or

print(random.randrange(5))
