brands = ["opel", "bmw", "mercedes"]

index = 0

for brand in brands:
    index += 1
    print(f"{index} - {brand}")

# enumarate

object = enumerate(brands)

print(type(object)) # Cevabımız: <class 'enumerate'>
print(list(object)) # Cevabımız: [(0, 'opel'), (1, 'bmw'), (2, 'mercedes')]

for i in enumerate(brands):
    print(i)
                        # Cevabımız:
                                    # (0, 'opel')
                                    # (1, 'bmw')
                                    # (2, 'mercedes')

for indx, value in enumerate(brands):
    print(indx, value)
                            # Cevabımız:
                                    # 0 opel
                                    # 1 bmw
                                    # 2 mercedes

for indx, value in enumerate(brands, 10):
    print(indx, value)
                                # Cevabımız:
                                    # 10 opel
                                    # 11 bmw
                                    # 12 mercedes

# zip

listOne = [1, 2, 3, 4, 5]
listTwo = ["a", "b", "c", "d", "e"]
listThree = [100, 200, 300, 400, 500]

print(list(zip(listOne, listTwo)))
# Cevabımız: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

print(list(zip(listOne, listTwo, listThree)))
# Cevabımız: [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(listOne, listTwo):
    print(item)

                                # Cevabımız:
                                    # (1, 'a')
                                    # (2, 'b')
                                    # (3, 'c')
                                    # (4, 'd')
                                    # (5, 'e')

for a, b, c in zip(listOne, listTwo, listThree):
    print(a, b, c)
    
                                # Cevabımız:
                                    # 1 a 100
                                    # 2 b 200
                                    # 3 c 300
                                    # 4 d 400
                                    # 5 e 500