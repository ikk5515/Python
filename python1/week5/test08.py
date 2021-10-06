scores = []

print("성적을 입력하세요. (q 입력시 종료)")

while True:
    data = input("성적: ")
    if data.lower() == 'q':
        break
    scores.append(float(data))
print(scores)
