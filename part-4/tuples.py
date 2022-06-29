# A tuple is a collection.
# tuples değiştirlemez bir listedir.
# https://www.w3schools.com/python/python_tuples.asp

_list = [1, 2, 3]
_tuple = (1, 2, 3)
_tuple_2 = 1, 2, 3
_tuple_3 = (1, "iki", True)

print(_list)
print(type(_list))

print(_tuple)
print(type(_tuple))

print(_tuple_2)
print(type(_tuple_2))

print(_tuple_3[0]) # Cevabımız: 1 / Listelerdeki gibi 0. İndexini yazdırıyoruz.

print(_list[0]) # Cevabımız: 1 / Tupels gibi 0. indexini yazdırıyoruz.

print(len(_list)) # Cevabımız: 3
print(len(_tuple)) # Cevabımız: 3

_list[0] = 5
print(_list) # Liste içerisindeki elemanlar değişebiliyor..

# _tuple[0] = 5 # Tuples değiştirilemez bir listedir.
# print(_tuple) # TypeError: 'tuple' object does not support item assignment / Hatası karşımıza geliyor.

_list.append(3)
print(_list)

# _tuple.append(5) # AttributeError: 'tuple' object has no attribute 'append' / Hatası karşımıza geliyor.
# print(_tuple)

print(_tuple_3.count(1)) # True = 1 / olduğu için .count(1) işlemimizin sonucu 2'dir.


_t = tuple([3, 4, 5]) # Ynei bir tuple listesi yapmış olduk.
print(_t) # Cevabımız: (3, 4, 5)