a = 5
b = 10
c = 20

print(a, b, c)

a += 5 # a = a + 5
print(a) # Cevabımız: a = 10

a -= 5 # a = a - 5
print(a) # Cevabımız: a = 5

a *= 5 # a = a * 5
print(a) # Cevabımız: a = 25

a //= 5 # a = a // 5
print(a) # Cevabımız: a = 5

a %= 5 # a = a % 5
print(a) # Cevabımız: a = 0

a **= 5 # a = a ** 5
print(a) # Cevabımız: a = 0

a /= 5 # a = a / 5
print(a) # Cevabımız: a = 0.0

d = 30

e = 25

d, e = e, d

print(d, e) # Cevabımız: 25 30

values = (1, 2, 3)
a, b, c = values
sonuc = values

print(a, b, c) # Cevabımız: 1 2 3
print(sonuc)

values_2 = (4, 5, 6, 7, 8)
a, b, *c = values_2 # Buradaki "*" işaretimizi koymamızın sebebimiz, yukarıda 3'ten fazla değer olduğundan dolayı "*" işareti koymamız gerekmektedir. ~ Geri kalan bütün değerler "c" içerisine liste şeklinde atanmıştır. ~ Eğer ki "c" içersinine atamak istemiyorsanız "a" veya "b" içerisine de atayabilirsiniz.

print(a, b, c) # Cevabımız: 4 5 [6, 7, 8]

values_3 = (8, 10, 11, 12, 13)
a, *b, c = values_3
print(a, b, c) # Cevabımız: 8 [10, 11, 12] 13