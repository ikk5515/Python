numbers = int(input("4자리의 정수 입력: "))

result = 0
for i in [1000, 100, 10, 1]:
    result += numbers // i
    numbers %= i

print(result)
