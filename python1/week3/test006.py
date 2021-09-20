cars = ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai']
print(cars)

cars.sort() # 오름차순 (정방향, asc)으로 정렬
print(cars)

cars.sort(reverse=True) # 내림차순 (역방향, desc)으로 정렬
print(cars)

print("*" * 60)

cars = ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai']
print(cars)

cars_copy = sorted(cars)
print(cars)
print(cars_copy)

cars_copy = sorted(cars, reverse=True)
print(cars_copy)

print("*" * 60)

cars = ['audi', 'tesla', 'benz', 'kia', 'lincoln', 'hyundai']
cars_copy = cars[:] # 복사
cars_copy.reverse()
print(cars)
print(cars_copy)