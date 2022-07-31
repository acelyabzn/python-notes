# 1- Girilen bir ssayının 50-100 arasında olup olmadığını kontrol ediniz.

number1 = int(input("1- Bir Sayı Giriniz: "))

if (100 > number1 > 50):
    print(f"100 > {number1} > 50")

else:
    print(f"{number1} Sayısı 50 ile 100 Arasında Değildir.")

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

number2 = int(input("2- Bir Sayı Giriniz: "))

if (-1 < number2) and (number2 % 2 == 1):
    print(f"{number2} Tek ve Pozitif bir sayıdır.")

elif (number2 == 0):
    print(f"{number2}'dır.")

else:
    print(f"{number2} Sayısı Tek veya Pozitif Bir Sayı Değildir.")

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız.

username = "acelyabazan"
password = "8888"

information1 = str(input("Kullanıcı Adınızı Giriniz: "))
information2 = input("Şifrenizi Giriniz: ")

if (information1 == username) and (information2 == password):
    print(f"{username} Hoş Geldiniz..")

else:
    print("Kullanıcı Adınız veya Şifreniz Yanlıştır. Lütfen Tekrar Deneyiniz..")

"""
Devam Edeceğim...
"""

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x = int(input("1- Bir Sayı Giriniz: "))
y = int(input("2- Bir Sayı Giriniz: "))
z = int(input("3- Bir Sayı Giriniz: "))

if (x > y > z):
    print(f"{x} > {y} > {z}")

elif (x > z > y):
    print(f"{x} > {z} > {y}")

elif (z > x > y):
    print(f"{z} > {x} > {y}")  

elif (z > y > x):
    print(f"{z} > {y} > {x}")  

elif (y > z > x):
    print(f"{y} > {z} > {x}")

elif (y > x > z):
    print(f"{y} > {x} > {z}")

else:
    print("Vermiş Olduğunuz İki Veya Üç Sayı Birbirine Eşittir.")

# 5- Kullanıcıdan 2 vize (%40) ve final (%60) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalde 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("1. Vize Notu: "))
vize2 = float(input("2. Vize Notu: "))
final = float(input("Final Notu: "))

result = ((vize1 + vize2 // 2) * 0.4) + (final * 0.6)

if (result >= 50 and final >= 50):
    print(f"{result} Tebrikler, Geçtiniz.")

elif (result < 50 ):
    print(f"{result} Notunuz Yeterli Değildir, Kaldınız.")

elif (final >= 70 and result >= 50):
    print(f"{result} Notunuz Ortslamanın Üstündedir, Geçtiniz.")

else:
    print()

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız.
# Formül (Kilo / Boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişini hangi guruba girmektedir.
# 0 - 18.4     => Zayıf
# 18.5 - 24.9  => Normal
# 25.0 - 29.9  => Fazla Kilolu
# 30.0 - 34.9  => Obez

name = input("Adınız: ")
weight = float(input("Kilonuz: "))
height = float(input("Boyunuz (Örneğin: 1.65): "))

index = weight / (height ** 2)
index2 = round(index, 4)

if (0 < index < 18.4):
    print(f" İndexsiniz: {index2} Zayıf Kategorisindesiniz.")

elif (18.5 < index < 24.9):
    print(f" İndexsiniz: {index2} Normal Kategorisindesiniz.")

elif (25.0 < index < 29.9):
    print(f" İndexsiniz: {index2} Fazla Kilolu Kategorisindesiniz.")

else:
    print(f" İndexsiniz: {index2} Obez Kategorisindesiniz.")