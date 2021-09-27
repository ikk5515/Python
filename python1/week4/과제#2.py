first_semester = float(input("1학기 학점: "))
second_semester = float(input("2학기 학점: "))

vol_time = int(input("봉사시간: "))

total = (first_semester + second_semester) / 2

if total >= 3.5 and vol_time >= 8:
    print("장학금 대상 여부 : ", True)
else:
    print("장학금 대상 여부 : ", False)