toplam = 0
urunler = [
    {"name":"iphone 8", "price":"4000"},
    {"name":"iphone 8 Plus", "price":"5000"},
    {"name":"iphone X", "price":"6000"},
    {"name":"iphone XR", "price":"7000"},
    {"name":"iphone 11", "price":"8000"},
    {"name":"samsung s10", "price":"6000"}
]

# 1- Tüm ürün bilgisini listeleyiniz.

for i in urunler:
    print(i.items())

# 2- Ürünlerin toplam fiyatı nedir?

for x in urunler:
    toplam = toplam + int(x["price"])

print(toplam)

# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz

for a in urunler:
    if (int(a["price"]) <= 6000):
        print(a)

# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz:

keyWords = input("Lütfen Anahtar Kelimeyi Aratınız: ")

for b in urunler:
    if (b["name"].find(keyWords.lower()) > -1):
        print(b["name"])