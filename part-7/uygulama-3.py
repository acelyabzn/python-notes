sayilar = [4, 6, 9, 10, 35, 57, 89, 125, 244]

# 1- sayilar listesini while ile ekrana yazdırın
a = 0

while (a < len(sayilar)):
    a += 10
    print(sayilar)

"""
Devam Edeceğim...
"""

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp tüm tek sayıları ekrana yazdırın.
baslangic = int(input("Başlangıç Değeri: "))
bitis = int(input("Bitiş Değeri: "))

i = baslangic

while i < bitis:
    i += 1
    if (i % 2 == 0):
        print(f"Tek Sayı: {i}")

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
b = 100

while (b > 0):
    b -= 1
    print(b)

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

sayilar = []
c = 0

while (c < 5):
    sayi = int(input("Sayı: "))
    sayilar.append(sayi)
    c += 1

sayilar.sort()
print(sayilar)