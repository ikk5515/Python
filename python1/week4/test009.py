print("놀이동산입장권")
age = int(input("니이: "))
tp = int(input("주간입장권(1) / 야간입장권(2): "))

# 1번 - 8세 이상이면 4000원, 나머지는 0원
price = 0

if age  >= 8:
    price = 4000
print(f"#1번 가격은 {price}원 입니다." ,end='\n\n')

# 2번 8세 이상이면 4000원(성인요금), 나머지는 0원(영유아요금)
if age >= 8:
    adult = "성인"
    price = 4000
else:
    adult = "영유아"
    price = 0
print(f"#2번 {adult}요금 - {price}원 입니다." ,end='\n\n')

# 3번 19세 이상이면 4000원(성인), 8~18세, 70세 이상이면 3000원(특별요금), 나머지는 0원(영유아)

if age < 8:
    adult = "영유아"
    price = 0
elif age <= 18:
    adult = "특별"
    price = 3000
elif age < 70:
    adult = "성인"
    price = 4000
else:
    adult ="특별"
    price = 3000
print(f"#3번 {adult}요금 - {price}원 입니다.", end='\n\n')


# 4번 19세 이상이면 4000원(성인), 8~18세, 70세 이상이면 3000원(특별요금), 나머지는 0원(영유아)

if age < 8:
    adult = "영유아"
    price = 0
elif age <= 18 or age >= 70:
    adult = "특별"
    price = 3000
else:
    adult = "성인"
    price = 4000
print(f"#4번 {adult}요금 - {price}원 입니다.", end='\n\n')


# 5번 19세 이상이면 4000원(성인), 8~18세, 70세 이상이면 3000원(특별요금), 나머지는 0원(영유아)
# 단, 야간의 경우 나이와 상관없이 모두 2000원

if age < 8:
    adult = "영유아"
    price = 0
elif tp == 1:    # 주간
    if age <= 18 or age >= 70:
        adult = "특별"
        price = 3000
    else:
        adult = "성인"
        price = 4000
else:          # 야간
    adult = "야간"
    price = 2000

print(f"#5번 {adult}요금 - {price}원 입니다.", end='\n\n')
