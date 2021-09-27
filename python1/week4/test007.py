# 변수 사용
'''
kor = 99
eng = 88
mat = 55
avg = (kor + eng + mat) / 3

print(f"{'과목':^4} {'점수':^4}")
print("=" * 12)
print(f"{'국어':^4}: {kor:>4}")
print(f"{'영어':^4}: {eng:>4}")
print(f"{'수학':^4}: {mat:>4}")
print(f"\n평균:, {avg:0.2f}")
'''

# 리스트 사용
'''
scores = [99, 88, 55]
avg = sum(scores) / len(scores)

print(f"{'과목':^4} {'점수':^4}")
print("=" * 12)
print(f"{'국어':^4}: {scores[0]:>4}")
print(f"{'영어':^4}: {scores[1]:>4}")
print(f"{'수학':^4}: {scores[2]:>4}")
print(f"\n평균:, {avg:0.2f}")
'''

# 리스트 + for
'''
lect = ('국어', '영어', '수학')
scores = [99, 88, 55]
avg = sum(scores) / len(scores)

print(f"{'과목':^4} {'점수':^4}")
print("=" * 12)

for i in range(3):
    print(f"{lect[i]:^4}{scores[i]:>4}")
print(f"\n평균:, {avg:0.2f}")
'''


#input 사용해서 점수 입력 받기

lect = ('국어', '영어', '수학', '과학')
scores = []
for l in lect:
    scores.append(int(input(f"{l} 점수: ")))
avg = sum(scores) / len(scores)

print(f"{'과목':^4} {'점수':^4}")
print("=" * 12)

for i in range(len(lect)):
    print(f"{lect[i]:^4}{scores[i]:>4}")
print(f"\n평균:, {avg:0.2f}")



# enumerate
lect = ('국어', '영어', '수학', '과학')
scores = []
for l in lect:
    scores.append(int(input(f"{l} 점수: ")))
avg = sum(scores) / len(scores)

print(f"{'과목':^4} {'점수':^4}")
print("=" * 12)

for i, lec in enumerate(lect):
    print(f"{lect:^4}{scores[i]:>4}")
print(f"\n평균:, {avg:0.2f}")
