# int
# float
# string
# bool

"""
x = int(input("x: "))
y = int(input("y: "))

print(type(x))
print(type(y))

toplam = x + y
print(toplam)
"""

import re


age = 17
weight = 59.5
name = "Açelya"
isStudent = True

# print(type(age))
# print(type(weight))
# print(type(name))
# print(type(isStudent))

# integer to float

result = float(age)

print(result)
print(type(result))

# float to integer

result = int(weight)

print(result)
print(type(weight))

# bool to string

result = str(isStudent)

print(result)
print(type(result))

# bool to integer

result = int(isStudent)

print(result)
print(type(result))

# True == 1