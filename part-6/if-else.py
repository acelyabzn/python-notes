if (5 > 10): # işlemimizin sonucu False olduğu için cevabımız erkana yazdırılmamaktadır.
    print("merhaba")

isLoggedin = True

if(isLoggedin == True):
    print("Hello World") # Cevabımız: Hello World

username = "acelyabazan"
password = "8888"

userinfo = str(input("Lütfen Kullanıcı AAdınınzı Giriniz: "))
passwordinfo = input("Lütfen Şifrenizi Giriniz: ")

if (userinfo == username) and (passwordinfo == password):
    print(f"{username} Hoş Geldiniz :)")

else:
    print("Kullanıcı Adınız veya Parolanız Yanlıştır Lütfen Tekrar Deneyiniz..")
