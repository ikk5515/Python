a = 1    # 지역변수


def vartest(a):    # vartest() 구역 내의 지역변수
    a = a + 1
    return a


a = vartest(a)
print(a)