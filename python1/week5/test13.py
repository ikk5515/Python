print("+++구구단 프로그램+++")

while True:
    data = input("\n구구단-단수(2-9): ")

    if data.strip().lower() == 'q':    # 종료 확인 - break
        break

    data = int(data)
    # if not(2 <= data <= 9)    # 범위 확인 - continue
    if 2 > data or data > 9:
        print("입력한 '단'이 범위를 벗어납니다.")
        continue
    for i in range(1,10):    # 1-9 구구단
        print(f"{data} * {i} = {data * i:>2}")

print("[종료]")
