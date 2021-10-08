def add_and_mul(a, b):
    return a + b, a * b


def add_and_mul2(a, b):
    return a + b    # return을 만나면 무조건 끝나서 아래 return은 실행X
    return a * b


a, b = add_and_mul(1, 2)
print(a, b)

a = add_and_mul(1, 2)
print(a)


b = add_and_mul2(1, 2)
print(b)




c = 1, 2
print(type(c))    # tuple