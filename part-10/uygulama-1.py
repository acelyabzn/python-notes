# 1- Kendisine gönderilen bir kelimeyi belirten kez ekranda gösteren foksiyonu yazınız.
def sayHello(word, number):
    print(word * number)

sayHello("Hello World!\n", 5)

# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def area(longSide, shortSide):
    areaCalculation = longSide * shortSide
    perimeterCalculation = 2 * (longSide + shortSide)

    print("The Area Is:", areaCalculation)
    print("The Perimeter Is:", perimeterCalculation)

area(7, 8)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random Modülü)

import random

guess = input("Heads or Tails: ")
randomM = random.choice(["heads", "tails"])

def headsOrTails(guess):

    if (guess == randomM):
        return f"{guess} It's True, You Won The Game"
            
    elif (guess != randomM):
        return f"{guess} It's False, You Lost The Game. Answer is {randomM}"

    else:
        return "You Have to Choose The Numbers 1 or 2"

resultThree = headsOrTails(guess)

print(resultThree)

# 6- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon yazınız.

isPrime = True
primeList = []

def primeNumbers(numberOne, numberTwo):
    for number in range(numberOne, numberTwo):
        if (number > 1):
            for h in range (2, number):
                if (number % h == 0):
                    break
                
            else:
                print(number)

primeNumbers(10, 20)


# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.


def numbers(number):
    listNumber = []

    for z in range(1, 10):
        if (number % z == 0):
            listNumber.append(z)
        
    return listNumber

print(numbers(15))