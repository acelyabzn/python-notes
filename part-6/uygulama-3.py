# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 yaşında ve eğitim durumu lise ya da üniversite olmalıdır.

from hashlib import new


name = input("İsminiz: ")
age = int(input("Yaşınız: "))
grade = input("Eğitim Durumunuz (Örenğin: Lise, Üniversite..)")

underage18 = (18 - age)

if (age >= 18) and (grade == "Lise", "lise", "Üniversite", "üniversite"):
    print(f"{name} Ehliyet Alabilecek Durumdasınız.")

elif (age <= 18):
    print(f"{name} Yaşınız Ehliyet Almak İçin Küçüktür. Lütfen {underage18} Yıl Sonra Tekrar Başvurunuz.")

elif (age >= 18) and (grade != "Lise", "lise", "Üniversite", "üniversite"):
    print(f"{name} Eğitim Durumunuz Ehliyet Almak İçin Uygun Değildir. Lütfen En Az Lise Diplomanız Olması Şartıyla Tekrar Başvurunuz.")

else:
    print(f"{name} Yanlış Bilgi Girdiniz. Lütfen Tekrar Deneyiniz.")

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisni yazdırınız.

grade1 = int(input("1. Yazılı Notunuz: "))
grade2 = int(input("2. Yazılı Notunuz:"))

newGrade = ((grade1 + grade2) // 2)

if (0 < newGrade < 24):
    print(f"Notunuz: {newGrade} Not Aralığınız: 0")

elif (25 < newGrade < 44):
    print(f"Notunuz: {newGrade} Not Aralığınız: 1")

elif (45 < newGrade < 54):
    print(f"Notunuz: {newGrade} Not Aralığınız: 2")

elif (55 < newGrade < 69):
    print(f"Notunuz: {newGrade} Not Aralığınız: 3")

elif (70 < newGrade < 84):
    print(f"Notunuz: {newGrade} Not Aralığınız: 4")

elif (85 < newGrade < 100):
    print(f"Notunuz: {newGrade} Not Aralığınız: 5")

else:
    print(f"{newGrade} Notunuzu Yanlış Girmişsinizdir. Lütfen Tekrardan Deneyiniz.")

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.

#   1. Bakım => 1. Yıl
#   2. Bakım => 2. Yıl
#   3. Bakım => 3. Yıl
#   ** Süre hesabının alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#   *** datatime modülünü kullanmanız gerekiyor.
#   (simdi) - (2018/8/1) => gün

year = int(input("Olduğunuz Yılı Giriniz: "))
month = int(input("Olduğunuz Ayı Giriniz: "))
day = int(input("Bugünün Günü Giriniz: "))

newDay = (day - 1)
newMonth = (month - 8)
newDay = (year - 2018)


newDate = (f"{newDay}.{newMonth}.{newDay}")

"""
Yapamadım :(
"""

import datetime

tarih = input('(2019/7/11)')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis')
elif (gun>365) and (gun<=365*2):
    print('2.servis')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis')
else:
    print('hatalı bilgi girdiniz.')