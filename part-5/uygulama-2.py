# 1- Girilen 2 sayıda hangisi büyüktür?

# 2- Girilen bir sayının tek mi çift miolduğunu yazdırın.

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.

# 4- Kullanıcıdan 2 vize (60%) ve final (40%) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# 5- Parola ve email bilgisini isteyipdoğruluğunu kontrol ediniz.
#    (email: info@sadikturan.com parola:12345)

"""
Önemli Not: if, elif ve else koşul ifadelerini daha işlemedim fakat araştırarak yaptım...
"""

# 1. İstek:
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if (sayi1 > sayi2):
    print(f"{sayi1} > {sayi2}")

elif (sayi2 > sayi1):
    print(f"{sayi2} > {sayi1}")

# 2. İstek:
sayi3 = int(input("3. Sayı: "))

if ((sayi3 % 2) == False):
    print(f"{sayi3} Çift Sayıdır.")

elif ((sayi3 % 2) == True):
    print(f"{sayi3} Tek Sayıdır.")

# 3. İstek:
sayi4 = int(input("4. Sayı: "))

if (sayi4 > -1):
    print(f"{sayi4} Pozitif Sayıdır.")

elif (sayi4 < -1):
    print(f"{sayi4} Negatif Sayıdır.")

elif (sayi4 == 0):
    print(f"{sayi4} Nötür Sayıdır.")

# 4. İstek:
vize1 = int(input("1. Vize Notunuzu Giriniz: "))
vize2 = int(input("2. Vize Notunuzu Giriniz: "))
final = int(input("Final Notunuzu Giriniz: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

if (ortalama >= 50):
    print(f"Not Ortalamanız: {ortalama} ~ Geçtiniz.")

elif (50 > ortalama):
    print(f"Not Ortalamanız: {ortalama} ~ Kaldınız.")

# 5. İstek:
email = input("Kayıt Yaptırmış Olduğunuz E-Mail Adresini Giriniz: ")
password = input("Kayıt Yaptırmış Olduğunuz Parolanızı Giriniz: ")

if (email == "info@sadikturan.com"):
    print("E-Mail Doğrudur.")

elif (email != "info@sadikturan.com"):
    print("E-Mail Yanlıştır.")

if (password == "12345"):
    print("Parola Doğrudur.")

elif (password != "12345"):
    print("Parola Yanlıştır.")

"""
Cevapların Hepsi Doğrudur Fakat Koşul İfadelerine Geçmediğimiz İçin Sadık Hocam Farklı Yapmıştır.
"""