names = ["Ahmet", "ali", "Çınar", "DeNiz"]
string = "Hello 12345 World"
years = [1983, 1999, 2008, 1956, 1986]
degrees = [20, 5, 15, -2, 0, -6]

# 1- 1-100 arasındaki sayılardan 12'ye tam bölünebilen sayı listesi oluşturunuz.

numbers = [x for x in range(1, 100) if ((x % 12) == 0)]
print(numbers,":", "Numbers Can Divisible By 12") # Answer: [12, 24, 36, 48, 60, 72, 84, 96] : Numbers Can Divisible By 12

# 2- names listesindeki her ismi küçük harfe çevirip tersten yazdırınız.

names = [y[::-1].lower() for y in names]
print(names) # Answer: ['temha', 'ila', 'ranıç', 'zined']

# 3- Verilen "string" içindeki rakamlari içeren bir liste oluşturunuz.

string = [z for z in string[6:11]]
print(string) # Answer: ['1', '2', '3', '4', '5']

# 4- "years" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
import datetime
now = datetime.datetime.now().year
years = [(now - q) for q in years]
print("Ages:", years) # Answer: Ages: [39, 23, 14, 66, 36]

# 5- "degrees" listesinde bulunan hava sıcaklık bilgisine göre eksi dere için buzlanma tehlikesi yazınız.

degrees = [a if (a >= 0) else ("Risk of Icing") for a in degrees]
print(degrees) # Answer: [20, 5, 15, 'Risk of Icing', 'Risk of Icing', 'Risk of Icing']