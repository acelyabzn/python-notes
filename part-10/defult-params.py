def sayHello(name, message="Hello"):
    print(f"{message}, {name}.")

sayHello("Açi", "Hello")
sayHello("Açi")

def exponentiation(base, expontent=2):
    return base ** expontent

result = exponentiation(3)

print(result)

def total(a, b):
    return a + b

def extraction(a, b):
    return a - b

def process(a, b, fn = total):
    return fn(a, b)

result = process(5, 3)

print(result)