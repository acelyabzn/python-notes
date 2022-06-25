website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- " Hello World " karakter dizisinin baş ve sonundaki boşluk karakterlerini silin.
 
# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

# 3- "kursAdi" karakter dizisinin tüm karakterlerini küçük harf yapın.

# 4- "website" içinde kaç tane a karakteri vardır? (count("a"))

# 5- "website" "www" ile başlayıp com ile bitiyor mu?

# 6- "website" içinde ".com" ifadesi var mı?

# 7- "kursAdi" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# 9- "kursAdi" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.

# 11- "kursAdi" karakter dizisini boşluk karakterlerinden ayırın.

# 1. İstek:
helloWorld = " Hello World "
helloWorld_2 = helloWorld.strip() # Cevabımız: "Hello World".
print(helloWorld_2)

# 2. İstek:
sadikTuran = "www.sadikturan.com"
deleted = sadikTuran.replace("www.", "").replace(".com", "") # Cevabımız: "sadikturan".
print(deleted)

# 3. İstek:
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
kursAdi_2 = kursAdi.lower() # Cevabımız: "python dersleri: sıfırdan i̇leri seviye python programlama."
print(kursAdi_2)

# 4. İstek:
website = "http://www.sadikturan.com"
website_2 = website.count("a") # Cevabımız: 2
print(website_2)

# 5. İstek:
website = "http://www.sadikturan.com"
website_3 = website.startswith("www") # Cevabımız: False
website_4 = website.endswith("com") # Cevabımız: True
print(website_3, website_4)

# 6. İstek:
website = "http://www.sadikturan.com"
website_5 = website.find(".com") # Cevabımız: 21
print(website_5)

# 7. İstek:
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
kursAdi_3 = kursAdi.isalpha() # Cevabımız: False
print(kursAdi_3)

# 8. İstek:
result = 'Contents'.center(50, '*')
print(result) # Cevabımız: *********************Contents*********************
print(len(result)) # Cevabımız: 50

# 9. İstek:
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
print(kursAdi.replace(" ", "-")) # Cevabımız: Python-Dersleri:-Sıfırdan-İleri-Seviye-Python-Programlama.

# 10. İstek:
helloWorld_3 = "Hello World"
result_2 = helloWorld_3.replace("World", "There") # Cevabımız: "Hello There".
print(result_2)

# 11. İstek:
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
print(kursAdi.split())

"""
Şimdi Cevapları Kontrol Ediyorum..
"""

# 1.  İstek: Doğru
# 2.  İstek: Sadık Hocam Farklı Yapmış Ama Sonuç Aynıdır. Doğru
# 3.  İstek: Doğru
# 4.  İstek: Doğru
# 5.  İstek: Doğru
# 6.  İstek: Doğru
# 7.  İstek: Doğru
# 8.  İstek: Doğru
# 9.  İstek: Doğru
# 10. İstek: Doğru
# 11. İstek: Doğru