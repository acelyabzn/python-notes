# Aldığım 2 tane öğrenciyi karşılaştıracağım..

ogrenciler = {}

# 1. Öğrenci:
ad = input("Öğrenci Adı: ")
soyad = input("Öğrenci Soy Adı: ")
okulNumara = int(input("Öğrencinin Okul Numarası: "))
notlarBir = int(input("Matematik 1. Sınavın Notu: "))
notlarIki = int(input("Matematik 2. Sınavın Notu: "))
notlarUc = int(input("Matematik 3. Sınavın Notu: "))

ogrenciler[okulNumara] = {
    "ad": ad,
    "soyad": soyad,
    "not_1": notlarBir,
    "not_2": notlarIki,
    "not_3": notlarUc
}

# 2. Öğrenci: 
ad = input("Öğrenci Adı: ")
soyad = input("Öğrenci Soy Adı: ")
okulNumara = int(input("Öğrencinin Okul Numarası: "))
notlarBir = int(input("Matematik 1. Sınavın Notu: "))
notlarIki = int(input("Matematik 2. Sınavın Notu: "))
notlarUc = int(input("Matematik 3. Sınavın Notu: "))

ogrenciler[okulNumara] = {
    "ad": ad,
    "soyad": soyad,
    "not_1": notlarBir,
    "not_2": notlarIki,
    "not_3": notlarUc
}

print(ogrenciler)

# Not Karşılaştırması:
numara = int(input("Öğrencinin Okul Numarası: "))
ogrencilerNew = ogrenciler[numara]

karsilastirma = (ogrenciler[numara]["not_1"] + ogrenciler[numara]["not_2"] + ogrenciler[numara]["not_3"]) // 3

x = ogrenciler[numara]["ad"]
y = karsilastirma

print(f"{x} Öğrencisinin Not Ortalaması: {y}")