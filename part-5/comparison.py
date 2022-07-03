# email, password => database

# email == "info@sadikturan.com"
# password == "12345"

a, b, c, d = 5, 5, 20, 4
sonuc = (a == b) # "==" operatörümüz "a" eşit eşit midir "b"'ye? sorusunu sormaktadır..
print(sonuc) # Cevabımız: True

sonuc = (a != b) # "!=" operatörümüz "a" eşit eşit değil midir "b"'ye? sorusunu sormaktadır..
print(sonuc) # Cevabımız: False

sonuc = (a == c) # "==" operatörümüz "a" eşit eşit midir "c"'ye? sorusunu sormaktadır..
print(sonuc) # Cevabımız: False

sonuc = (a > c) # ">" operatörümüz "a" büyük müdür "c"? sorusunu sormaktadır..
print(sonuc) # Cevabımız: False

sonuc = (c >= a) # ">=" operatörümüz "a" büyük eşit midir "c"? sorusunu sormaktadır..
print(sonuc) # Cevabımız: True

sonuc = (c <= a) # "<=" operatörümüz "a" küçük eşit midir "c"? sorusunu sormaktadır..
print(sonuc) # Cevabımız: True

username = "acelyabazan"
password = "12345"

sonucAci = (username == "acelyabazan")
print(sonucAci) # Cevabımız: True

sonucAci = (username != "acelyabazan")
print(sonucAci) # Cevabımız: False

"""
Not:    True = 1
        False= 0
"""

sonuc = (True == 1)
print(sonuc) # Cevabımız: True 
print(int(True)) # Cevabımız: 1

sonuc = (False == 0)
print(sonuc) # Cevabımız: True 
print(int(False)) # Cevabımız: 0

sonuc = (False + True + 50)
print(sonuc) # Cevabımız: 51