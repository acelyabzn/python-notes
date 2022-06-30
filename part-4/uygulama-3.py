# 1- 3 ürün bilgisini (id, ad, fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.


# 1. İstek:
"""1. Ürünün Bilgileri"""

urunler = {}# Boş bir Dictionary

ad_bilgisi = input("1. Ürünün Adı: ")
id_bilgisi = input("1. Ürünün ID: ")
fiyat_bilgisi = input("1. Ürünün Fiyatı: ")

urunler[id_bilgisi] = {
    "ad": ad_bilgisi,
    "fiyat": fiyat_bilgisi
}

"""2. Ürünün Bilgileri"""

ad_bilgisi = input("2. Ürünün Adı: ")
id_bilgisi = input("2. Ürünün ID: ")
fiyat_bilgisi = input("2. Ürünün Fiyatı: ")

urunler[id_bilgisi] = {
    "ad": ad_bilgisi,
    "fiyat": fiyat_bilgisi
}

"""3. Ürünün Bilgileri"""

ad_bilgisi = input("3. Ürünün Adı: ")
id_bilgisi = input("3. Ürünün ID: ")
fiyat_bilgisi = input("3. Ürünün Fiyatı: ")

urunler[id_bilgisi] = {
    "ad": ad_bilgisi,
    "fiyat": fiyat_bilgisi
}

print(urunler)

# 2. İstek:

id = input("Artmak İstediğiniz Ürün ID Numarasını Giriniz:")
urunNew = urunler[id]

print(f"id: {id}")
print(f"Ürün Adı: {urunNew['ad']}")
print(f"Ürün Fiyatı: {urunNew['fiyat']}")