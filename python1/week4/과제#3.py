select  = int(input("1: 사각, 2: 삼각, 3: 원 "))

if select == 1:
    width = float(input("가로 입력: "))
    length = float(input("세로 입력: "))
    total = width * length
elif select == 2:
    base = float(input("밑변 입력: "))
    height = float(input("세로 입력: "))
    total = (base * height) / 2
elif select == 3:
    r = float(input("반지름 입력: "))
    total = 3.14 * (r**2)
else:
    print("잘못된 입력입니다.")
print(f"도형의 넓이 = {total:0.2f}")