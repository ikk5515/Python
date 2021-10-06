import random

rnd_number = random.randint(1, 100)  # 임의의 수 생성
count = 0

print("+++숫자를 맞쳐보세요.(1~100)+++")
while True:
    user_number = int(input("입력: "))  # 사용자의 입력 -> 정수변환
    count += 1
    if rnd_number > user_number:
        print("숫자가 작습니다.")
    elif rnd_number < user_number:
        print("숫자가 큽니다.")
    else:
        break

print(f"{user_number}가 정답입니다. 도전 횟수는 {count}회 입니다.")