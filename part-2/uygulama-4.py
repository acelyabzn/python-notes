"""
Bir aracın  Km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
mil = km / 1.609344
"""

km = float(input("Aracınızın Km cisninden gittiği yolu yazın:"))

mile = km / 1.609344

# round yuvarlama işlemi yapmaya yarıyor
mile = round(mile, 2)

# 1. yol
result = "Km = " + str(km) + "  " + "Mil = " + str(mile)
print(result)

# 2. yol
print("Aracınızın mil cinsinden gittiği yol:", mile)