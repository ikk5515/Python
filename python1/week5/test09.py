scores = {}

print("이름과 성적을 입력하세요. ('q'입력시 종료)")

while True:
    name = input("이름: ")
    if name.lower() == 'q':
        break
    score = float(input("성적: "))
    scores[name] = score

    for name, score in scores.items():
        print(f"{name}: {score}")
