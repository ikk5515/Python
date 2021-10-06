pets = ["dog", "cat", "dog", "rabbit", "goldfish", "snake", "dog"]
print(pets)

# 삭제할 동물 명 받고...
name = input("동물명: ").strip().lower()

# while 이용해서 동물 삭제
while name in pets:
    pets.remove(name)


'''for pet in pets:
    if pet == name:
        pets.remove(pet)'''


print(pets)
