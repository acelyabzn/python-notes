def sayHello(name):
    return "Hello, " + name

resultOne = sayHello("Açi")

print(resultOne)



def addition(a, b):
    return a + b

resultTwo =  addition(7, 1)

print(resultTwo)



import datetime

def ageCalculator(year, birthYear):
    return year - birthYear

year = datetime.datetime.now().year

age = ageCalculator(year, 2004)

print(age)



import datetime


def howManyYearsToRetire(name, birthYear):
    year = datetime.datetime.now().year
    age = year - birthYear

    remainingTime = 65 - age

    if (remainingTime > 0):
        print(f"{name}, you have {remainingTime} years to retire.")
    
    else:
        print(f"{name}, you already retire.")

new = howManyYearsToRetire("Açi", 2004)