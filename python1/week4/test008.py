car = 'KIA'

print(car == "Kia")    # False
print(car.lower() == 'kia')   # True
print(car.lower() != 'bmw')   # True

print("=" *10)

myage = 22
yourage = 19

print(myage >= 21 and yourage >= 21)   # False
print(myage >= 21 or yourage >= 21)    # True

print("=" *10)

cars = ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai']
print(car in cars)   # False
print(car not in cars)    # True
print(car.lower() in cars)   # True
print(car.lower() not in cars)   # False

print("=" *10)

t1 = True
t2 = False
t3 = (3 <= 2)  # False
t4 = 5 != 3  # True

year = 2021
# 윤년, 4의 배수인데, 100의 배수가 아닌 연도, 또는 400의 배수
t5 = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(t1, t2, t3, t4, t5)
