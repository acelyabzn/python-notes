isimler = ["Ada", "Yiğit", "Hasan", "Beril"]
yaslar = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

# 2- "Sena" değerini listenin başına ekleyiniz.

# 3- "Yiğit" ismini listeden siliniz.

# 4- "Yiğit" isminin indexi nedir?

# 5- "Beril" listenin elemanı mıdır?

# 6- Liste elemanlarını ters çevirin.

# 7- Liste elemanlarını alfabetik olarak sıralayınız.

# 8- yaslar listesinin rakamsal büyüklüğe göre sıralayınız.

# 9- str = "Iphone X, Iphone XR" karakter dizisini listeye çeviriniz.

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir?

# 11- yaslar dizisinde kaç tane 1998 değeri vardır?

# 12- yaslar dizisinin tüm elemanlarını siliniz.

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.


# 1. İstek:
isimler_1 = ["Ada", "Yiğit", "Hasan", "Beril"]
isimler_1.append("Cenk")
print(isimler_1) # Cevabımız: ['Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']

# 2. İstek:
isimler_2 = ['Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
isimler_2.insert(0, "Sena")
print(isimler_2) # Cevabımız: ['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']

# 3. İstek:
isimler_3 = ['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
isimler_3.pop(2)
print(isimler_3) # Cevabımız: ['Sena', 'Ada', 'Hasan', 'Beril', 'Cenk']

# 4. İstek:
isimler_4 = ['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
print(isimler_4.index("Yiğit")) # Cevabımız: 2

# 5. İstek:
isimler_5 = ['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
if "Beril" in isimler_5:
    print("Evet. Beril Listenin Bir Elemanıdır.") # Cevabımız: Evet. Beril Listenin Bir Elemanıdır.

# 6. İstek:
isimler_6 = ['Sena', 'Ada', 'Yiğit', 'Hasan', 'Beril', 'Cenk']
isimler_6.reverse()
print(isimler_6) # Cevabımız: ['Cenk', 'Beril', 'Hasan', 'Yiğit', 'Ada', 'Sena']

# 7. İstek:
isimler_7 = ['Cenk', 'Beril', 'Hasan', 'Yiğit', 'Ada', 'Sena']
isimler_7.sort()
print(isimler_7) # Cevabımız: ['Ada', 'Beril', 'Cenk', 'Hasan', 'Sena', 'Yiğit']

# 8. İstek: 
yaslar_1 = [1998, 2000, 1998, 1987]
yaslar_1.sort()
print(yaslar_1) # Cevabımız: [1987, 1998, 1998, 2000]

# 9. İstek:
# str = ["Iphone X", "Iphone XR"]
# print(str) # Cevabımız: ['Iphone X', 'Iphone XR']

# Doğrusu:
str = "Iphone X,Iphone XR "
sonucNew = str.split(",")
print(sonucNew)

# 10. İstek:
yaslar_2 = [1998, 2000, 1998, 1987]
sonuc_1 = max(yaslar_2)
sonuc_2 = min(yaslar_2)
print(f"Listedeki En Büyük Rakam: {sonuc_1}")
print(f"Listedeki En Küçük Rakam: {sonuc_2}")

# 11. İstek:
yaslar_3 = [1998, 2000, 1998, 1987]
print(yaslar_3.count(1998)) # Cevabımız: 2

# 12. İstek:
yaslar_4 = [1998, 2000, 1998, 1987]
yaslar_4.clear()
print(yaslar_3 ) # Cevabımız: []

# 13. İstek:
markalar = []

markaOne = input("1. Marka Bilgisi: ")
markalar.append(markaOne)

markaTwo = input("2. Marka Bilgisi: ")
markalar.append(markaTwo)

markaThree = input("3. Marka Bilgisi: ")
markalar.append(markaThree)

print(markalar) # Cevabımız: ['Yazdığımız Marka', 'Yazdığımız Marka', 'Yazdığımız Marka']



"""
Şimdi Cevapları Kontrol Ediyorum..
"""

# 1. İstek:  Doğru
# 2. İstek:  Doğru
# 3. İstek:  Doğru
# 4. İstek:  Doğru
# 5. İstek:  Doğru
# 6. İstek:  Doğru
# 7. İstek:  Doğru
# 8. İstek:  Doğru
# 9. İstek:  Yanlış (Soruyu Yanlış Anlamışım)
# 10. İstek: Doğru
# 11. İstek: Doğru
# 12. İstek: Doğru
# 13. İstek: Doğru