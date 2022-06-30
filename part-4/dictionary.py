# Key - Value
# 41 plakasının Kocaeli olduğunu Python Dictionary kullanarak basit bir şekilde gösterebiliriz.

"""Liste Yöntemi İle Yapabiliriz Fakat Karıştırma Oranımız Çok Fazla.."""

city = ["Kocaeli", "Istanbul"]
plakalar = [41, 34]

print(plakalar[0], city[0]) # Cevabımız: 41 Kocaeli
print(plakalar[1], city[1]) # Cevabımız: 34 Istanbul

print(city.index("Istanbul")) # Cevabımız: 1
print(plakalar[city.index("Istanbul")]) # Cevabımız: 34

"""Dictionary Yöntemi İle İşimiz Daha Kolay.."""

plakalar_dict = {
    "Kocaeli": 41,
    "Istanbul": 34
}

print(plakalar_dict) # Cevabımız: {'Kocaeli': 41, 'Istanbul': 34}
print(plakalar_dict["Istanbul"]) # Cevabımız: 34
print(plakalar_dict["Kocaeli"]) # Cevabımız: 41

plakalar_dict["Rize"] = 53 # Cevabımız: {'Kocaeli': 41, 'Istanbul': 34, 'Rize': 53}
# Bu şekilde Dictionary içerisine bir key ve value ekleyebiliriz..
print(plakalar_dict)

# plakalar_dict["Izmir"] = 35 # Cevabımız: {'Kocaeli': 41, 'Istanbul': 34, 'Rize': 53, 'Izmir': 35}
# print(plakalar_dict)

# Örneğin yanlışlıkla Izmir için plakasınıa 36 yazdık. Bunu nasıl düzeltebiliriz? Hemeeeenn gösteriyoruum:
plakalar_dict["Izmir"] = 36 # Cevabımız: {'Kocaeli': 41, 'Istanbul': 34, 'Rize': 53, 'Izmir': 36}
print(plakalar_dict)

plakalar_dict["Izmir"] = 35 # Cevabımız: {'Kocaeli': 41, 'Istanbul': 34, 'Rize': 53, 'Izmir': 35}
print(plakalar_dict)

students = {
    90: {
        "Ad": "Açelya",
        "Soyad": "Bazan",
        "Yas": 17,
        "Notlar": [50, 40, 80]
    },
    95: {
        "Ad": "Çınar",
        "Soyad": "Turan",
        "Yas": 4
    },
    100: {
        "Ad": "Berre",
        "Soyad": "Abacı",
        "Yas": 16
    }
}

print(students[100]) # Cevabımız: {'Ad': 'Berre', 'Soyad': 'Abacı', 'Yas': 16}

sonuc = students[90]["Ad"] # Cevabımız: Açelya
print(sonuc)

notes = students[90]["Notlar"][2] # Cevabımız: 80
print(notes) 

notes_ort = (students[90]["Notlar"][0] + students[90]["Notlar"][1] + students[90]["Notlar"][2]) // 3
print(notes_ort) # Cevabımız: 56 - 3 notun ortalamasını aldım..