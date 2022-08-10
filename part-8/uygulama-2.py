import random
"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukaru ifadeler ile buldurmaya çalışın.
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""


randomNumber = random.randrange(1,100)
print(randomNumber)

x = 0
life = int(input("How many life points do you want: "))
lifePoint = life


while (lifePoint > 0):
    lifePoint -= 1
    x += 1
    guess = int(input("Guess the number: "))
    print("Your Life Point is:", lifePoint)

    if (randomNumber == guess):
        print("Congratulations! You find the number. You total score:", {100 - (100 / lifePoint) * (x - 1)})
        break

    elif (randomNumber > guess):
        print("Increase the value of the number.")

    else: 
        print("Decrease the value of the number.")
    
    if (lifePoint == 0):
        print("Game Over..")
        print("The Number is:", randomNumber)