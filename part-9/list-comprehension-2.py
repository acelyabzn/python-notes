numbers = [1, 5, 8, 9, 15, 44]
conclusion = []

# for i in numbers:
#     if (i % 2 == 0):
#         conclusion.append(i)
    
# print(conclusion) # Answer: [8, 44]

newConclusion = [i for i in numbers if (i % 2 == 0)]
print("Even Numbers:", newConclusion) # Answer: Even Numbers: [8, 44]

newConclusion = [i for i in numbers if (i % 2 == 1)]
print("Odd Numbers:", newConclusion) # Answer: Odd Numbers: [1, 5, 9, 15]

newConclusion = [i if (i % 2 == 0) else ("Odd Numbers") for i in numbers]
print(newConclusion) # Answer: ['Odd Numbers', 'Odd Numbers', 8, 'Odd Numbers', 'Odd Numbers', 44]

prices = [1000, 3000, 5000, 0, 4000]
taxes = []

# for x in prices:
#     if (x > 0):
#         taxes.append(x * 1.18)
# print(taxes) # Answer: [1180.0, 3540.0, 5900.0, 4720.0]

taxes = [x * 1.18 for x in prices if (x > 0)]
print(taxes) # Answer: [1180.0, 3540.0, 5900.0, 4720.0]

taxes = [x * 1.18 if (x > 0) else ("Tax Not Calculated") for x in prices]
print(taxes) # Answer: [1180.0, 3540.0, 5900.0, 'Tax Not Calculated', 4720.0]

# result = []
# for b in range(3):
#     for y in range(3):
#         result.append((b, y))

# print(result) # Answer: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

result = [(b, y) for b in range(3) for y in range(3)]
print(result) # Answer: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]