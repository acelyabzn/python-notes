opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opelObj["marka"] # Cevabımız: Opel
print(sonuc)

sonuc1 = opelObj.get("marka") # Cevabımız: Opel
print(sonuc1)

print(opelObj) # Cevabımız: {'marka': 'Opel', 'model': 'Corsa', 'yil': 2020} 

for x in opelObj:
    print(x)
# Cevabımız:    marka
#               model
#               yil

for x in opelObj:
    print(opelObj[x])
# Cevabımız:    Opel
#               Corsa
#               2020

for x in opelObj.values(): # Bu metodumuz opelObj içerisindeki bütün values yazdırıyor..
    print(x)
# Cevabımız:    Opel
#               Corsa
#               2020

for x, y in opelObj.items():  # Bu metodumuz opelObj içerisindeki bütün itemleri yazdırıyor..
    print(x, y) # "x bilgisi: key", "y bilgisi: value" denk gelmektedir.
# Cevabımız:    marka Opel
#               model Corsa
#               yil 2020

sonucNew = "marka" in opelObj # "'marka' bilgisi opelObj içersininde var mı?" sorusuna cevap vermektedir.
print(sonucNew) # Cevabımız: True

sonucNew2 = len(opelObj) # "opelObj kaç elemanlıdır?" sorusuna cevap vermektedir.
# Not: "marka": "Opel" bu 1 tane eleman olarak sayılıyor.
print(sonucNew2) # Cevabımız: 3

opelObj["renk"] = "kırmızı" # Cevabımız: {'marka': 'Opel', 'model': 'Corsa', 'yil': 2020, 'renk': 'kırmızı'}
print(opelObj)

opelObj.pop("renk") # Cevabımız: {'marka': 'Opel', 'model': 'Corsa', 'yil': 2020}
print(opelObj)

opelObj.popitem() # Son Itemimizi siliyor..
print(opelObj) # Cevabımız: {'marka': 'Opel', 'model': 'Corsa'}

# del opelObj / Bu komutumuz opelOpj Dictionary silmektedir..
# print(opelObj) / Fakat hiç Dictiyonary sildiğimiz için print yaptırdığımızda "NameError" hatası almaktayız..

# opelObj.clear() # Cevabımız: {}
# Not: Bu metot bütün elemanları siler.

obj = opelObj # opelObj referans.
print(obj) # Cevabımız: {'marka': 'Opel', 'model': 'Corsa'}

obj["marka"] = "Mazda"
print(obj) # Cevabımız: {'marka': 'Mazda', 'model': 'Corsa'} / obj üzerinde değişiklik yapmış olduk.

"""
ÖNEMLİ NOT: obj = opleObj adresleri aynıdır. Bu sebepten dolayı obj üzerinde veya opelObj üzerinde yapılan değişiklikler birbirilerini etkiler.
"""

obj_2 = opelObj.copy() # Kopyalamış Olduk..
print(obj_2)

"""
ÖNEMLİ NOT 2: opelObj.copy() yaptığımızda ise obj_2 üzerinde değişiklik yaparsak hiç bir şekilde opelObj etkilemez.
"""

opelObj.update({
    "marka": "Bmw", 
    "renk": "kırmızı"
})
print(opelObj) # Cevabımız: {'marka': 'Bmw', 'model': 'Corsa', 'renk': 'kırmızı'}