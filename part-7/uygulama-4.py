# Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesinin içinde saklayınız.
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri while ile listeleyin.

i = 0
adet = int(input("Kaç Adet Ürün Eklemek İsitiyorsunuz: "))
urunler = []

while (i < adet):
    urunAdi = input("Ürün Adı: ")
    fiyat = input("Ürün Fiyatı: ")
    urunler.append({
        "urunAdi":urunAdi,
        "fiyat":fiyat
    })
    i += 1
# for urun in urunler:
# print(f"Ürün Adı: {urun['urunAdi']} Ürün Fiyatı: {urun['fiyat']}")

a = 0
while (a < len(urunler)):
    print(f"Ürün Adı: {urunler[a]['urunAdi']} Ürün Fiyatı: {urunler[a]['fiyat']}")
    a += 1
