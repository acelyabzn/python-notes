# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız.

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalde 70 alındığında ortalamanın önemi olmasın.

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız.
# Formül (Kilo / Boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişini hangi guruba girmektedir.
# 0 - 18.4     => Zayıf
# 18.5 - 24.9  => Normal
# 25.0 - 29.9  => Fazla Kilolu
# 30.0 - 34.9  => Obez

# 1. İstek:
sayi1 = int(input("Sayı Giriniz:"))

if (100 > sayi1 > 50):
    print(f"{sayi1} 50 ile 100 arasındadır.")

else:
    print(f"{sayi1} 50 ile 100 arasında değildir.")

# 2. İstek:
sayi2 = int(input("Sayı Giriniz:"))

if (-1 < sayi2 and (sayi2 % 2 == 1)):
    print(f"{sayi2} Pozitif ve Tek Sayıdır.")

else:
    print(f"{sayi2} Pozitif ve Tek Sayı Değildir.")

# 3. İstek:

username = "acelyabzn"
password = "1234"

type1 = str(input("Kullanıcı Adınızı Giriniz:"))
type2 = input("Şifrenizi Giriniz:")

if ((type1 == username) and (type2 == password)):
    print("Kullanıcı Adı ve Parolanız Doğrudur.. Hoş Geldiniz")

elif ((type1 != username) and (type2 == password)):
    print("Kullanıcı Adınız Yanlıştır.. Tekrar Deneyiniz.")

elif ((type1 == username) and (type2 != password)):
    print("Parolanız Yanlıştır.. Tekrar Deneyiniz.")

else:
    print("Kullanıcı Adınız ve Parolanız Yanlıştır.. Tekrar Deneyiniz.")

# 4. İstek:
sayi3 = int(input("1. Sayı Giriniz:"))
sayi4 = int(input("2. Sayı Giriniz:"))
sayi5 = int(input("3. Sayı Giriniz:"))

if (sayi3 > sayi4 > sayi5):
    print(f"{sayi3} > {sayi4} > {sayi5}")

elif (sayi5 > sayi4 > sayi3):
    print(f"{sayi5} > {sayi4} > {sayi3}")

elif (sayi4 > sayi5 > sayi3):
    print(f"{sayi4} > {sayi5} > {sayi3}")

elif (sayi3 > sayi5 > sayi4):
    print(f"{sayi3} > {sayi5} > {sayi4}")

elif (sayi5 > sayi3 > sayi4):
    print(f"{sayi5} > {sayi4} > {sayi3}")

elif (sayi5 > sayi3 > sayi4):
    print(f"{sayi5} > {sayi4} > {sayi3}")

else:
    (print("iki veya üç tane sayı birbirine eşittir."))

"""
Birazdan Devam Edeceğim...
"""

"""
Devamm...
"""

# 5. İstek:
vize1 = int(input("1. Vize Notu: "))
vize2 = int(input("2. Vize Notu: "))
final = int(input("Final Notu: "))

sonuc = ((((vize1 + vize2) / 2) * 0.6) + (final * 0.4))
sonuc2 = ((((vize1 + vize2) / 2) * 0.6) + (final))

if ((sonuc >= 50) and (final >= 70)):
    print(f"{sonuc2} Geçerli Not Ortalaması. Final Notunuz 70 veya 70'in Üzerindedir")

elif (sonuc >= 50):
    print(f"{sonuc} Geçerli Not Ortalaması.")

elif (sonuc <= 50):
    print(f"{sonuc} Geçersiz Not Ortalaması.")

# 6. İstek:
name = str(input("Adınız: "))
kilo = int(input("Kilonuz: "))
height = float(input("Boy Uzunluğunuz: "))

formül = (kilo / (height ** 2))

if (0 <= formül <= 18.4):
    print(f"{name} Vücut Inedxiniz {formül} (Zayıf) Kategorisindesiniz.")

elif (18.5 <= formül <= 24.9):
    print(f"{name} Vücut Inedxiniz {formül} (Normal) Kategorisindesiniz.")

elif (25.0 <= formül <= 29.9):
    print(f"{name} Vücut Inedxiniz {formül} (Fazla Kilolu) Kategorisindesiniz.")

elif (30.0 <= formül <= 34.9):
    print(f"{name} Vücut Inedxiniz {formül} (Obez) Kategorisindesiniz.")

"""
Koşul İfadelerine Geçmediğimiz İçin Sadık Hocam Farklı Yapmıştır.
"""
