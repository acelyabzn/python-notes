sayilar = [1, 2, 3, 6, 8, 9, 15, 20]

for i in sayilar:
    print(i)

for i in sayilar:
    print("Merhaba")

isimler = ["Ali", "Deniz", "Açi"]

for isim in isimler:
    print(isim)

name = "Açelya Bazan"

for a in name:
    print(a)

_tuple = [(1, 2), (4, 5), (6, 7)]

for x in _tuple:
    print(x)

for x, y in _tuple:
    print(x, y)

_dict = {"k1":1, "k2":2, "k3":3 }

for b in _dict:
    print(b)
    
for b in _dict:
    print(_dict[b])

for b in _dict.values():
    print(b)
    
for b, z in _dict.items():
    print(b, z)