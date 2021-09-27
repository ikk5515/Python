#반지금 입력
#높이 입력
#수식으로 계산하고
#출력

r = float(input("반지름 입력: "))
h = float(input())

v = 3.141592 * (r ** 2) * h
print(f"원기둥의 부피: {v:0.2f}")
