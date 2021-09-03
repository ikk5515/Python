while True:
    year = int(input('연도: '))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('올해는 윤년입니다.')
            else:
                print('올해는 평년입니다.')
        else:
            print('올해는 윤년입니다.')
    else:
        print('올해는 평년입니다.')