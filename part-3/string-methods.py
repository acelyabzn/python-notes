msg = "Python kursumuza hoş geldiniz. Ben Açelya Bazan"

sonuc = msg.upper() # Butün harfleri büyük yapmamızı sağlar. .upper()
print(sonuc)

sonuc2 = msg.lower() # Butün harfleri küçük yapmamızı sağlar. .lower()
print(sonuc2)

sonuc3 = msg.title() # Harflerin başını büyük yapmamızı sağlar. .title()
print(sonuc3)

sonuc4 = msg.capitalize() # Sadece cümlenin harfi başını büyük yapmamızı sağlar. .capitalize()
print(sonuc4)

sonuc5 = "abc".islower() # Bütün harfler küçük mü diye bakar. .islower()
print(sonuc5)

sonuc6 = "  abc  ".strip() # Baştaki ve sondaki boşlukları siliyor. .strip()
print(sonuc6)

sonuc7 = msg.split() # Köşeli parantez oluyor ve her bir karakteri string yapıyor. .split()
print(sonuc7)
print(sonuc7[0]) # Cümledeki Stringin 0. indeksini yazdırmak için kullanılıyor. 
print(sonuc7[1]) # Cümledeki Stringin 1. indeksini yazdırmak için kullanılıyor.

sonuc8 = msg.split(".") # Cümleyi noktadan itibaren ikiye ayır. 
print(sonuc8)

sonuc9 = msg.split()
sonuc9 = "-".join(sonuc9) # Aralara "-" koyarak kelimeleri birleştiriyor. "-".join(sonuc9)
print(sonuc9)

index = msg.index("hoş") # Aramış olduğumuz kelime 17. index'ten başlamaktadır. msg.index("hoş")
print(index)

sonuc10 = msg.startswith("P") # String hangi harf ile başlarsa onun True  ya da False olarak değerlendiriyor. Örneğin "P" harfi ile başlıyor, msg.startswith("P") yazdığımızda işlemimizin sonucu True.
print(sonuc10)

sonuc11 = msg.startswith("y") # String hangi harf ile başlarsa onun True  ya da False olarak değerlendiriyor. Örneğin "P" harfi ile başlıyor, msg.startswith("y") yazdığımızda işlemimizin sonucu False.
print(sonuc11)

sonuc12 = msg.endswith("n") # String hangi harf ile biterse onun True  ya da False olarak değerlendiriyor. Örneğin "n" harfi ile bitiyor, msg.startswith("n") yazdığımızda işlemimizin sonucu True.
print(sonuc12)

sonuc13 = msg.endswith("a") # String hangi harf ile biterse onun True  ya da False olarak değerlendiriyor. Örneğin "n" harfi ile bitiyor, msg.startswith("a") yazdığımızda işlemimizin sonucu False.
print(sonuc13)


sonuc14 = msg.replace("Açelya", "Açi") # Hangi kelimeyi değiştirmek istersek msg.replace() metotunu kullanıyoruz.
print(sonuc14)

sonuc15 = msg.replace(" ", "-").replace("ş", "s").replace(".","") #Birden fazla kelimeyi kulanmak istersek bu şekilde kodumuzu yazıyoruz.
print(sonuc15)