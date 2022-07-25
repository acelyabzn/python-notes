# yaş 1= 18 ve manzuniyet == "lise" ya da menzuniyet == üniversite

# 1. Yol:
x = 10

sonuc = 5 < x < 15
print(sonuc) # Cevabımız: True

# 2. Yol: "and" operatörü (ve)
sonuc = (x > 5) and (x < 15) # İlk parentez içerisindeki işlemimiz True, ikinci parentez içerisindeki işlemimizde True ise cevabımız True.
# True ve True => True
# False ve True => False
# False ve False => False

hak = 3
devam = "e"
print(hak > 0) and (devam == "e")

# "or" operatörü (veya)

(x > 0) # Sayı pozitiftir.
(x % 2 == 0) # Çift sayıdır.

sonucNew = (x > 0) or (x % 2 == 0) 
# True veya True => True
# False veya True => True
# False veya False => False
print(sonucNew)

# "not" operatörü (soruyu tersten sormak)
sonucNot = not(x > 0)
print(sonucNot) # Cevabımız: False