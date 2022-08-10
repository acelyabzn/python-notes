# def addition():
#     return f"Addition: {10 + 20}"

# a = addition()

# print(a)

def addiction():
    return 10 + 20

resultOne = addiction() + 50

print(resultOne)


import datetime

def ageCalculator():
    now = datetime.datetime.now().year
    return now - 2004

resultTwo = ageCalculator()

print("Your Age Is", resultTwo)


def hour():
    import datetime
    return datetime.datetime.now().hour

minute = datetime.datetime.now().minute

a = hour()
b = minute

print(f"{a}.{b}")

def sayGoodMorning():
    if (a < 12):
        return "Good Morning"
    else:
        return "Hello"

print(f"{sayGoodMorning()}, {a}.{b} o'clock")