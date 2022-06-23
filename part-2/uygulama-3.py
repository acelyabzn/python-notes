"""
Daire Alanı   : πr²
Daire Çevresi : 2πr
** Yarı çapı verilerin bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)
"""

r = float(input("Dairenin Yarı Çapını Girin:"))

pi = 3.14
alan = pi * (r ** 2)
cevre = 2 * pi * r

# 1. yol
result = "Alan: " + str(alan) + " " + "Çevre: " + str(cevre)
print(result)

# 2. yol
print("Dairenin Alanı:", alan)
print("Dairenin Çevresi:", cevre)