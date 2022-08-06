name = "Açelya Bazan"

for letter in name:
    if (letter == "e"):
        continue
    print(letter)   # Cevabımız:
                                # A
                                # ç
                                # l
                                # y
                                # a

                                # B
                                # a
                                # z
                                # a
                                # n

for letter in name:
    if (letter == "e"):
        break
    print(letter)
                    # Cevabımız:
                                # A
                                # ç

i = 0
while (i < 5):
    if (i == 3):
        break
    print(i)
    i += 1
print("Döngü Bitti.")

                    # Cevabımız:
                                # 0
                                # 1
                                # 2
                                # Döngü Bitti.

while (i < 5):
    i += 1
    if (i == 3):
        continue
    print(i)
print("Döngü Bitti.")
                    # Cevabımız:
                                # 4
                                # 5
                                # Döngü Bitti.

# 1- 100 arasındaki çift sayılar toplamı.
b = 0
total = 0

while (b <= 100):
    b += 1
    if (b % 2 == 0):
        continue
    total += b
print(f"Total: {total}")
# Cevabımız: Total: 2601