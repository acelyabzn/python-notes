toplam = 0
sayilar = [1, 5, 15, 35, 57, 72]

# 1- sayilar listesindeki her bir elemanı yazdırın.
 
for x in sayilar:
    print(x)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır?

for sayi in sayilar:
    if ((sayi % 5) == 0):
        print(f"{sayi} 5'in Katıdır.")

# 3- Sayilar listesinde sayiların toplamı kaçtır?

for y in range(0, len(sayilar)):
    toplam = toplam + sayilar[y]
# https://mertmekatronik.com/python-range-fonksiyonu / Range fonksiyonu mantığı burada anlatılmıştır.
print(f"Sayıların Toplamı: {toplam}")

# 4- Sayilar listesindeki çift sayıların karesini alınız.

for b in sayilar:
    if ((b % 2) == 0):
        print(b ** 2)

urunler = ["iphone 8", "iphone X", "iphone XR", "samsung S10"]

# 5- urunler listesindeki tüm ürünlerin 2. karakterlerini ekrana yazdırın.

for a in urunler:
    print(a[1:2])

# 6- urunler listesindeki içinde iphone geçen kaç ürün vardır.

for i in urunler:
    print(i.count("iphone"))
