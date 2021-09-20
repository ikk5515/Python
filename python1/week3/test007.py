scores = []  # list()

for data in range(1, 6, 1):
    scores.append(int(input(f'{data}번: ')))

'''
scores.append(int(input('1번: ')))
scores.append(int(input('2번: ')))
scores.append(int(input('3번: ')))
scores.append(int(input('4번: ')))
scores.append(int(input('5번: ')))
'''

number = 0

for score in scores:
    number += 1
    print(f"{number}번 학생 점수: {score}")
    
print("*" * 50)

for idx in range(len(scores)):
    print(f"{idx+1}번 학생 점수: {scores[idx]}")

    
avg = sum(scores) / len(scores)
print("총 평균: ", avg)
print("최고 점수: ", max(scores))
print("최저 점수: ", min(scores))

avg = sum(scores) / len(scores)
