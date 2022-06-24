# BOJ_1110_더하기_사이클

n = int(input())
number = n
count = 0

while True:
    a = number // 10 + number % 10          # 각 자리수를 더해줌
    b = (number % 10) * 10 + a % 10         # 더하기 전 오른쪽 수 + 주어진 수의 오른쪽 수
    number = b
    count += 1
    if number == n:
        print(count)
        break