sayilar = [2, 5, 7, 9]

# for => collection
# 1 - 100 => koşul => while
i = 0

while (i < 10):
    i += 1
    print(i)


# 1'den 100'e kadar olan tek sayıları ekrana yazdırıyoruz..
while (i <= 100):
    if (i % 2 == 1):
        print("Tek Sayı:", i)
# 1'den 100'e kadar olan çift sayıları ekrana yazdırıyoruz..
    else: 
        print("Çift Sayı:", i)
    i += 1


username = ""
print(bool(username)) # Cevabımız: False

usernameNew = "a"
print(bool(usernameNew)) # Cevabımız: True

userName = ""
while not userName:
    userName = input("Kullanıcı Adınız: ")
print(f"Girdiğiniz Kullanıcı Adınız: {userName}")