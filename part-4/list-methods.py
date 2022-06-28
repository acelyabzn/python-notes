sayilar = [1, 5, 8, 9, 3, 45]
harfler = ["a", "b", "e", "s", "a", "y"]

sonuc = min(sayilar) # min() metotunu kullanırsak listenin içerisindeki elemanın minimumunu buluyor.
print(sonuc) # Cevabımız: 1

sonuc_2 = max(sayilar) # max() metotunu kullanırsak listenin içerisindeki elemanın maximumunu buluyor.
print(sonuc_2) # Cevabımız: 45

sayilar.append(88) # .append() metodumuz listenin içerisine eleman eklemektedir.
sonuc_3 = sayilar
print(sonuc_3) # Cevabımız: [1, 5, 8, 9, 3, 45, 88]

sayilar.insert(3, 5) # insert() metodumuz hem eleman eklemektedir hem de eklemek olduğumuz elemanın yerini ayarlayabilmekteyiz.
# Örneğin: .insert(3, 5) 
#           3: Elemanın Yerini 3 Yerine Yazıyoruz.
#           5: Hangi Elemanı Liste İçerisine Koyacağımızı 5 Yerine Yazıyoruz.
# ÖNEMLİ NOT: Eğer birden fazla .insert() metotunu kullanacaksak her zaman en baştaki listeye göre bakmalıyız.

sonuc_4 = sayilar
print(sonuc_4)

sayilar.pop() # -1 elemanını siler.
sayilar.pop(0) # 0 elamnını siler.
sonuc_5 = sayilar

print(sonuc_5) # Cevabımız: [5, 8, 5, 9, 3, 45]

sayilar_2 = [5, 8, 5, 9, 3, 45]

sayilar.sort() # Sıralar.
harfler.sort() # Sıralar.
sayilar_2.reverse() # Sıralamayı Ters Yapar.

sonuc_6 = sayilar
sonuc_7 = sayilar_2
sonucNew = harfler

print(sonuc_6)  # Cevabımız: [3, 5, 5, 8, 9, 45]
print(sonuc_7) # Cevabımız: [45, 3, 9, 5, 8, 5]
print(sonucNew) # Cevabımız: ['a', 'a', 'b', 'e', 's', 'y']

print(sonuc_5.count(5)) # sayilar = [5, 8, 5, 9, 3, 45] liste elemanlarının içerisinde kaç tane 5 var sorusunu .count(5) cevaplamaktadır.

print(sonucNew.count("a")) # harfler = ['a', 'a', 'b', 'e', 's', 'y'] liste elemanlarının içerisinde kaç tane 5 var sorusunu .count("a") cevaplamaktadır.

print(sonuc_6)
print(sonuc_6.index(5)) # sayilar = [3, 5, 5, 8, 9, 45] liste elemanlarının içerisinde 5 sayısı kaçıncı sıradadır .index(5) metotu bunu göstermektedir.

sayilarNew = [1, 5, 8, 9, 3, 45]
sayilarNew.clear() # Bütün liste elemanlarını silmiş oluruz.
print(sayilarNew) # Cevabımız: []