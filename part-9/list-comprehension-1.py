listOne = [10, 4, 7, 9, 70]
numbers = []

# [expression for item in list]

numbers = [i for i in range(10)]
print(numbers) # Answer: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [i*2 for i in listOne]
print(numbers) # Answer: [20, 8, 14, 18, 140]

name = "Açi"
names = ["Açi", "hazal", "Berre", "BeYza"]

conclusion = [c.upper() for c in name]
print(conclusion) # Answer: ['A', 'Ç', 'I']

conclusion = [str(a) for a in listOne]
print(conclusion) # Answer: ['10', '4', '7', '9', '70']

conclusion = [x.lower() for x in names]
print(conclusion) # Answer: ['açi', 'hazal', 'berre', 'beyza']