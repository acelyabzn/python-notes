a, b, c = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamının farkı nedir?

# 2- "c"'nin "b"'ye kalansız bölümünü hesaplayınız.

# 3- (a, b, c) toplamının mod 3'ü nedir?

# 4- "b"'nin "a". kuvvetini hesaplayınız.

# sayilar = 1, 5, 7, 10, 3
# 5- a, *b, c = sayilar işlemine göre "c"'nin küpü kaçtır?

# 6- a, *b, c = sayilar işlemine göre "b"'nin değerleri toplamı kaçtır?

# 1. İstek:
deger = int(input("1. Sayı Değerini Giriniz: "))
deger2 = int(input("2. Sayı Değerini Giriniz: "))

deger *= deger2

toplam = a + b + c

fark = deger - toplam 
print(fark) # Cevabımız: Girdiğimiz değerlere göre değişiyor.

# 2. İstek:
c //= b
print(c) # Cevabımız: 2

# 3. İstek:
toplamNew = a + b + c

toplamNew %= 3
print(toplamNew)

# 4. İstek:
b **= a
print(b)

# 5. İstek:
sayilar = (1, 5, 7, 10, 3)

a, *b, c = sayilar
print(a, b, c)

c **= 3
print(c)

# 6. İstek:
print(b[0] + b[1] + b[2])


"""
Şimdi Cevapları Kontrol Ediyorum..
"""

# 1. Doğru
# 2. Doğru
# 3. Doğru
# 4. Doğru
# 5. Doğru
# 6. Doğru