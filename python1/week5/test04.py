print("이름을 입력하세. (단, quit 입력 시 종료")

while True :
    name = input("이름: ").strip().lower()

    if name == "quit":
        break           # 본인이 소속되어 있는 반복문 탈출
    else:
        print(name)
