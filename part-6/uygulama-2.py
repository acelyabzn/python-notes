# Bir aracın yakıt tipine göre (benzin, dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulama yazınız.

benzinFiyat = 6.69
dizelFiyat = 5.86

toplamYakitUcreti = 0

yakitTüketimi = float(input("100 k'deki Ortalama Yakıt Tüketimi: "))
gidelecekYol = float(input("Gidelecek Yol Kaç Km: "))
yakitTipi = input("Yakıt Tipiniz: ")

toplamYakitTuketimi = (gidelecekYol * (yakitTüketimi / 100))

if (yakitTipi == "benzin") or (yakitTipi == "Benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi

elif (toplamYakitTuketimi == "dizel") or (toplamYakitTuketimi == "Dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi

else:
    print("Yanlış Yakıgt Tipi Girdiniz, Lütfen Tekrar Deneyiniz.")

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)