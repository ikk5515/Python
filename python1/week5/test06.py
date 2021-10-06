print("1~n사이의 숫자 중 홀수의 합 (단, n의 최대값은 1000) ")
endpoint = int(input("n: "))
sum = 0

for number in range(0, 1001):
    if number % 2 == 0:
        continue
    if number > endpoint:
        break
    sum += number

print(sum)
