# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:28:45 2019

@author: Vince
"""

# Printing:: Basically your bread and butter to display information you want to see on the console.
# This is also useful for debugging (helping you identify errors)

#Printing a user defined string
print("Hello World") #Python will always convert what's inside the parenthesis as a string
print("\n ----------------------------------------- ")

#Variables : name them whatever you want as long as it is not a KEYWORD
print("Variable Section:")
variable = 1            # ambigous data type
variable2 = 2.0         # python is smart enough to determine this is a float
variable3 = "three"     # The " " will tell python that this is a string
print("variable")
print(variable)
print(variable2)
print(variable3)
print("\n ----------------------------------------- ")

#Casting
print("Casting Section")
variable2 = int(variable2)
print(variable2)
print("\n ----------------------------------------- ")

#Casting and concatination
print("Casting and Concatination")
print(str(variable2) + variable3)
variable4 = str(variable2) + " " + variable3
print(variable4)

#Practical print 
print("The value of variable4 is: " + str(variable4))
print("\n ----------------------------------------- ")

# Lists
print("Lists")
empty_list = []         # define an empty list
value_list = [1,2,3]   
string_list = ["hello", "world"]

print(empty_list)
print(value_list)
print(string_list)
print("\n ----------------------------------------- ")

#accessing specific index
print ("item in index 2 for value_list is: " + str(value_list[2]))

# Operations
x = 10
y = 8.8
z = 3.0

w = z + y
print (w) 
print("if you do not need to store the value of z+y you can print " + str(z+y))
print("you can even do it from a list! Remember our list value list? We can add entry 0 and 1 together and get: " + str(value_list[0] + value_list[1]))
print("even var x with a list element: " + str (x + value_list[2]))