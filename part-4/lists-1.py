msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan"
print(msg[0]) # 0. İndex: P

msg_2 = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan".split() # Bir Stringin İçerisinde Birden Fazla Stringi Köşeli parantezler içerisine alıyor.

print(msg_2[0]) # 0. Dize: Python
print(msg_2) # Cevabımız: ['Python', 'Kursumuza', 'Hoş', 'Geldiniz.', 'Ben', 'Sadık', 'Turan']

sayilar = [1, 3, 5, 7, 9] # Liste
sonuc = sayilar

print(sonuc)
print(type(sonuc))

isimler = ["açi", "açelya", "bazan"] # Liste
sonuc = isimler

print(sonuc)
print(type(sonuc))

listeAçi = ["Açelya", 17]

print(listeAçi)

aciAd = listeAçi[0]
aciYas = listeAçi[1]

print("Kişinin Adı:", aciAd)
print("Kişinin Yaşı:", aciYas)

ogrenciler = [["Açelya", 17], ["Berre", 16]]
print(ogrenciler)

ogrenciler_2 = [listeAçi, ["Berre", 16]]
print(ogrenciler_2)

ogrenciAd_1 = ogrenciler[0] [0] # 0. İndex, 0. Eleman
ogrenciAd_2 = ogrenciler[1] [0] # 1. İndex, 0. Eleman

print(ogrenciAd_1)
print(ogrenciAd_2)