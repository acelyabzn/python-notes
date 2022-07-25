# 1- Girilen bir sayının 50-100 arasınnda olup olmadığını kontrol ediniz.

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
sayi_1 = int(input("1. Sayı:"))

if (50 < sayi_1 and sayi_1 < 100):
    print(f"{sayi_1} ~Sayı 50 ile 100 arasındadır")

elif (sayi_1 < 50 and sayi_1 > 100):
    print(f"{sayi_1} ~Sayı 50 ile 100 arasında değildir.")

# 2. İstek:
sayi_2 = int(input("2. Sayı:"))

if (sayi_2 > 0 and sayi_2 % 2 == 1):
    print(f"{sayi_2} Sayısı tek ve pozitif bir sayıdır.")
