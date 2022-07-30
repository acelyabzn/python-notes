# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y) # Cevabımız: True
print(x == z) # Cevabımız: True

print(x is y) # Cevabımız: True
print(x is z) # Cevabımız: False

a = [1, 2, 3]
b = [2, 4]

print(a is b) # Cevabımız: False
print(a is not b) # Cevabımız: True

# Membership Operator: in

c = ["banana", "apple"]
print("banana" in c) # Cevabımız: True

name = ["Açelya"]
print("A" in name) # Cevabımız: False
print("A" not in name) # Cevabımız: True