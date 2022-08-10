# 1- Çarpım tablosu hazırlayınız.

i = 0
x = 1

multiplicationTable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for a in range(1,11):
    for b in range(1,11):
        print(f"{a} x {b} =",b * a)

    
# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
#   "Asal Sayı" 1 veya kendisi hariç tam böleni olmayan sayılara denir.

primeNumbers = int(input("Please Enter a Number: "))

isPrime = True

if (primeNumbers == 1):
    isPrime = False

for z in range(2, 10):
    if ((primeNumbers % z) == 1):
        isPrime = False
        break
    
if isPrime:
    print(primeNumbers, "is a Prime Number.")

else:
    print(primeNumbers, "is not a Prime Number.")
