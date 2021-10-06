import random

rnd_number = random.randint(1, 100)  # 임의의 수 생성
count = 0

print("+++숫자를 맞쳐보세요.(1~100)+++")
for i in range(0, 10):
    user_number = int(input("입력: "))  # 사용자의 입력 -> 정수변환
    count += 1
    if count >= 10:
        print(f"{rnd_number}가 정답입니다.")
        print("도전 실패!")
        break
    else:
        if rnd_number > user_number:
            print("숫자가 작습니다.")
        elif rnd_number < user_number:
            print("숫자가 큽니다.")
        else:
            print("성공했습니다!")
            print(f"{user_number}가 정답입니다. 도전 횟수는 {count}회 입니다.")
            break