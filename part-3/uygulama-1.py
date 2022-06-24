website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır?

# 2- 'website' içinden www karakterlerini alın.

# 3- 'website' içinden com karakterlerini alın.

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterini alın.

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.

# 6- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

# 7- 'abc' ifadesini yan yana 3 defa yazdırın.

name, surname, age, job = "Sadık","Turan", 37, "eğitimci"

# 8- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

# 1. İstek:
print(len(kursAdi)) # Cevabımız 58 karakter bulunmaktadır.

# 2. İstek:
print(website[7:10]) # Cevabımız "www".

# 3. İstek:
print(website[-3:]) # Cevabımız "com".

# 4. İstek:
# print(kursAdi[15:-15]) # Cevabımız ": Sıfırdan İleri Seviye Pyth" (emin değilim).

# 4. İstek Doğrusu:
sonuc1 = kursAdi[0:15]
print(sonuc1)
sonuc2 = kursAdi[:15]
print(sonuc2)
sonuc3 = kursAdi[-15:]
print(sonuc3)

# 5. İstek:
print(kursAdi[::-1]) # Cevabımız ".amalmargorP nohtyP eyiveS irelİ nadrıfıS :irelsreD nohtyP".

# 6. İstek:
# w = "W"
# helloWorld = f"Hello {w}orld"
# print(helloWorld) # Cevabımız "Hello World".

# 6. İstek Doğrusu:
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s) # Cevabımız "Hello World".

# 7. İstek:
abc = "abc "
multiplication = abc * 3
print(multiplication) # Cevabımız "abcabcabc".

# 8. İstek:
name, surname, age, job = "Sadık","Turan", 37, "eğitimci"

print("Benim Adım {} {}, Yaşım {} ve mesleğim {}.".format(name, surname, age, job)) # Cevabımız "Benim Adım Sadık Turan, Yaşım 37 ve mesleğim eğitimci.".


"""
Şimdi Cevapları Kontrol Ediyorum..
"""

# 1. İstek: Doğru
# 2. İstek: Doğru
# 3. İstek: Doğru (Sadık Hocam daha farklı yapmış ama sonuç aynıdır.)
# 4. İstek: Yanlış(Soruyu Yanlış Anlamışım.(Doğrusu Düzeltildi.))
# 5. İstek: Doğru
# 6. İstek: Yanlış(Yeni Bir Bilgi Öğrendim.)
# 7. İstek: Doğru
# 8. İstek: Doğru