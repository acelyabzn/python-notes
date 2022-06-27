diller = ["Python", "C#", "Java", "Javascript"]

sonuc = diller

print(sonuc[0]) # Cevabımız: Python
print(sonuc[-1]) # Cevabımız: Javascript

print(sonuc[0:2]) # Cevabımız: ['Python', 'C#']
print(sonuc[::-1]) # Cevabımız: ['Javascript', 'Java', 'C#', 'Python']

print(type(sonuc)) # Cevabımız: <class 'list'>
print(sonuc) # Cevabımız: ['Python', 'C#', 'Java', 'Javascript']

diller_2 = ["Python", "C#", "Java", "Javascript"]
print(diller_2) # Cevabımız: ['Python', 'C#', 'Java', 'Javascript']

diller_2[-1] = "React"
print(len(diller_2))
print(diller_2) # Cevabımız: ['Python', 'C#', 'Java', 'React']


diller_3 = ["Python", "C#", "Java", "Javascript"]
sonucYeni = diller_3
sonucYeni = diller_3 + ["Angular", "Vuejs"]
print(sonucYeni)



# DAHA İŞLEMEMİŞ OLDUĞUM KONULAR                 

# if bloğu => Koşul İfadeleri:
if "Python" in diller:
    print("evet")

# Döngüler:
for x in diller:
    print(x) # Cevabımız:   # Python
                            # C#
                            # Java
                            # Javascript

del diller [-1] #Cevabımız: ['Python', 'C#', 'Java']
print(diller)