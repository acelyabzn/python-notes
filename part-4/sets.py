# Bugüne kadar öğrenmiş olduğum liste tipleri aşağıdaki gibidir.

# list
# tuple
# dictionary
# sets

meyveler = {"elma", "kiraz", "kavun", "üzüm" }
sebzeler = {"bezelye", "soğan" }

sonuc = meyveler
sonuc2 = meyveler

print(sonuc) # Sets i"ndexlenemez ve sıralanamaz"..
# Cevabımız: {'kavun', 'kiraz', 'elma', 'üzüm'} ~Görmüş olduğunuz gibi yazdığımız sıralamada print olmadı..

sonuc2 = "elma" in meyveler
print(sonuc2) # Cevabımız: True

meyveler.add("karpuz") # Bu metotumuzda ise "karpuz" eklemiş bulunmaktayız fakat nagi sıraya eklediğini bilemeyiz..
print(sonuc) 

meyveler.update(["vişne", "kavun"]) # Vişne eklenir fakat kavun listemiz içerisinde olduğu için kavun 1 eleman olarak gözükür..
print(sonuc)

meyveler.remove("karpuz") # Cevabımız: {'elma', 'kavun', 'üzüm', 'kiraz', 'vişne'}
print(sonuc)

print(len(meyveler)) # Cevabımız: 5

meyveler.pop() # Herhangi bir eleman siliniyor.
print(sonuc)

# meyveler.clear() # Cevabımız: set()
# print(sonuc)

sonuc = meyveler.union(sebzeler) # Cevabımız: {'bezelye', 'elma', 'üzüm', 'kavun', 'soğan', 'vişne'} ~ İki listeyi birleştirmemizi sağlayan .union() metotumuzu kullanıyoruz..
print(sonuc)