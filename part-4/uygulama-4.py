'''
player 1:
    id              => 1
    name            => Cristiano Ronaldo
    yearOfBirth     => 1985
    nationality     => Portugal
    current_team    => Portugal
    history         => Juventus, Real Madrid, Portugal

player 1:
    id              => 2
    name            => Lionel Messi
    yearOfBirth     => 1987
    nationality     => Argentina
    current_team    => Barcelona
    history         => Barcelona, Argentina, Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
# 2- id' e göre arama yapınız.
# 3- id' e göre bilgi kayıt siliniz.

# 1. İstek:
players = {}

id = input("Oyuncu ID: ")
name = input("Oyuncu Ad: ")
yearOfBirth = input("Oyuncunun Doğduğu Yıl: ")
nationality = input("Oyuncunun Vatandaşlığı: ")
current_team = input("Oyuncunun Takımı: ")
history = input("Oyuncunun Oynadığı Takımlar: ")

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history
    }
})

id = input("Oyuncu ID: ")
name = input("Oyuncu Ad: ")
yearOfBirth = input("Oyuncunun Doğduğu Yıl: ")
nationality = input("Oyuncunun Vatandaşlığı: ")
current_team = input("Oyuncunun Takımı: ")
history = input("Oyuncunun Oynadığı Takımlar: ")

players.update({
    id: {
        "name": name,
        "yearOfBirth": yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history
    }
})

print(players)

# players = {'1': 
# {
#     'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': 'Juventus, Real Madrid, Portugal'
# },

# '2': {
#     'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': 'Barcelona, Argentina, Portugal'
# }}

# 2. İstek:
id = input("Aratmak İstediğiniz Oyuncunun ID Numarasını Giriniz: ")
idNew = players.get(id)

yas = 2022 - int(idNew['yearOfBirth'])

print("Oyuncunun Adı:", idNew['name'])
print("Oyuncunun Doğduğu Yıl:", idNew['yearOfBirth'])
print("Oyuncunun Yaşı:", yas)
print("Oyuncunun Vatandaşlığı:", idNew['nationality'])
print("Oyuncunun Takımı:", idNew['current_team'])
print("Oyuncunun Geçmişte Oynadığı Takımlar:", idNew['history'])

# 3. İstek:
id = input("Silmek İstediğiniz Oyuncu ID Numarasını Giriniz: ")
idNew_2 = players.pop(id)

print(players)