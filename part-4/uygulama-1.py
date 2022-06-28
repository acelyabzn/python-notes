# 1- "Samsung S5, Samsung S6, Samsung S7, Samsung S8" elemanlarına sahip bir liste oluşturunuz.

# 2- Liste kaç elemanlıdır?

# 3- Listenin ilk ve son elemanı nedir?

# 4- "Samsung S5" değerini "Samsung S9" ile değiştirin.

# 5- "Samsun S6" listenin bir elemanı mıdır?

# 6- Listenin -3 indexindeki değer nedir?

# 7- Listenin ilk 2 elemanını alın.

# 8- Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.

# 9- Listenin üzerine "Iphone X" ve "Iphone XR"  değerlerini ekleyin.

# 10- Listenin son elemanını silin.

# 11- Liste elemanlarını tersten yazdırın.

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

    # kullaniciA: Yiğit Bilgi 2010, (70, 60, 70)
    # kullaniciB: Sena  Turan 1999, (80, 80, 70)
    # kullaniciC: Ahmet Turan 1998, (80, 70, 90)

# 13- Liste elemanlarını ekrana yazdırınız.



# 1. İstek:
phones_1 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(phones_1) # Cevabımız: ['Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8']

# 2. İstek:
phones_1 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(len(phones_1)) # Cevabımız: 4

# 3. İstek:
ilkEleman = phones_1[0]
sonEleman = phones_1[-1]

print("İlk Eleman:", ilkEleman) # Cevabımız: İlk Eleman: Samsung S5
print("Son Eleman:", sonEleman) # Cevabımız: Son Eleman: Samsung S8

# 4. İstek:
phones_2 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
del phones_2[0]
newPhones = ["Samsung S9"] + phones_2

print(newPhones) # Cevabımız: ['Samsung S9', 'Samsung S6', 'Samsung S7', 'Samsung S8']

# 5. İstek:
phones_1 = ['Samsung S9', 'Samsung S6', 'Samsung S7', 'Samsung S8']
if "Samsung S6" in phones_1:
    print("Samsung S6 in there!") # Cevabımız: yes in there!

# 6. İstek:
phones_1 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(phones_1[-3]) # Cevabımız: Samsung S6

# 7. İstek:
phones_2 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
print(phones_2[0:2]) #Cevabımız: ['Samsung S5', 'Samsung S6']

# 8. İstek:
phones_3 = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]
del phones_3[-1]
del phones_3[-2]
newPhones_2 = phones_3 + ["Samsung S9", "Samsung S10"]
print(newPhones_2) # Cevabımız: ['Samsung S5', 'Samsung S7', 'Samsung S9', 'Samsung S10']

# 9. İstek:
Iphones = newPhones_2 + ["Iphone X", "Iphone XR"]
print(Iphones) # Cevabımız: ['Samsung S5', 'Samsung S7', 'Samsung S9', 'Samsung S10', 'Iphone X', 'Iphone XR']

# 10. İstek:
del Iphones[-1]
print(Iphones) # Cevabımız: ['Samsung S5', 'Samsung S7', 'Samsung S9', 'Samsung S10', 'Iphone X']

# 11. İstek:
Iphones_2 = ['Samsung S5', 'Samsung S7', 'Samsung S9', 'Samsung S10', 'Iphone X']
print(Iphones_2[::-1]) # Cevabımız: ['Iphone X', 'Samsung S10', 'Samsung S9', 'Samsung S7', 'Samsung S5']

# 12. İstek:
kullaniciA = [["Yiğit", "Bilgi"], [2010], [70, 60, 70]]
kullaniciB = [["Sena", "Turan"], [1999], [80, 80, 70]]
kullaniciC = [["Ahmet", "Turan"], [1998], [80, 70, 90]]

# 13. İstek:
# Yiğit Bilgiler
yigitAdSoyad = kullaniciA[0]
yigitDogumYili = kullaniciA[1]
yigitNot = kullaniciA[-1]
print("Ad, Soy Ad:", yigitAdSoyad)
print("Doğum Yılı:", yigitDogumYili)
print("Ders Not Ortalaması:", yigitNot)

# Sena Bilgiler
senaAdSoyad = kullaniciB[0]
senaDogumYili = kullaniciB[1]
senaNot = kullaniciB[-1]
print("Ad, Soy Ad:", senaAdSoyad)
print("Doğum Yılı:", senaDogumYili)
print("Ders Not Ortalaması:", senaNot)

ahmetAdSoyad = kullaniciC[0]
ahmetDogumYili = kullaniciC[1]
ahmetNot = kullaniciC[-1]
print("Ad, Soy Ad:", ahmetAdSoyad)
print("Doğum Yılı:", ahmetDogumYili)
print("Ders Not Ortalaması:", ahmetNot)

# 13. İstek Farklı Yöntem: Bunu yaparken zorlandım çünkü daha for döngülerine geçmedik..
ogrenciA = ["Yiğit","Bilgi",2010,[70, 60, 70]]
ogrenciB = ["Sena","Turan",1999,[80, 80, 70]]
ogrenciC = ["Ahmet","Turan",1998,[80, 70, 90]]

ogrenciler = [ogrenciA, ogrenciB, ogrenciC]


for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyAd = ogrenci[1]
    yas = 2022 - ogrenci[2]
    notOrtalama = (ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) // 3
    print(f"Ad: {ad} | Soy Ad: {soyAd} | Yaş: {yas} | Not Ortalaması: {notOrtalama}")

# Cevabımız:

# Ad: Yiğit | Soy Ad: Bilgi | Yaş: 12 | Not Ortalaması: 66
# Ad: Sena | Soy Ad: Turan | Yaş: 23 | Not Ortalaması: 76
# Ad: Ahmet | Soy Ad: Turan | Yaş: 24 | Not Ortalaması: 80

"""
Şimdi Cevapları Kontrol Ediyorum..
"""

# 1. İstek:  Doğru
# 2. İstek:  Doğru
# 3. İstek:  Doğru
# 4. İstek:  Doğru (Sadık Hocam Farklı Yapmış Ama Cevap Aynı.)
# 5. İstek:  Doğru
# 6. İstek:  Doğru
# 7. İstek:  Doğru
# 8. İstek:  Doğru (Sadık Hocam Farklı Yapmış Ama Cevap Aynı.)
# 9. İstek:  Doğru
# 10. İstek: Doğru
# 11. İstek: Doğru
# 12. İstek: Doğru
# 13. İstek: Doğru (Sadık Hocam Farklı Yapmış. Soruyu Sanırım Yanlış Anlamışım Ama Mantık Aynı.)