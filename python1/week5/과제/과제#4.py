score = int(input("점수: "))
if score < 0 or score > 100:
    input("0~100 사이의 점수를 입력해주세요.")
else:
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
    print(f"학점:{grade}")
