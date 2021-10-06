import datetime

cur_year = datetime.datetime.today().year
year = int(input("태어난 연도: "))    # 태어난 연도 입력 -> 정수
age = (cur_year - year + 1)    # 나이 계산


if 26 >= age >= 20:    # 나이에 따른 결과를 생성
    grade = '대학생'
elif 20 > age >= 17:
    grade = '고등학생'
elif 17 > age >= 14:
    grade = '중학생'
elif 14 > age > 8:
    grade = '초등학생'
else:
    grade = '학생이 아닙니다.'

print(f"결과: {grade}")    # 결과 출력
