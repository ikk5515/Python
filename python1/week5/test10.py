# 점수 입력
# 정수로 변환
score = int(input("점수: "))

if score >= 90:    # 90 ~ A
    grade = 'A'
elif score >= 80:    # 80 ~ B
    grade = 'B'
elif score >= 70:    # 70 ~ C
    grade = 'C'
elif score >= 60:    # 60 ~ D
    grade = 'D'
else:    # F
    grade = 'F'

print("학점: " + grade)    # 출력
print("학점: ", grade)       # 형태가 다름
print("학점: %s"% grade)    # 방법1
print("학점:{0}".format(grade))     # 방법2
print(f"학점:{grade}")    # 방법3
