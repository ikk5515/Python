# BOJ_2292_벌집
import sys

n = int(sys.stdin.readline())
count = 1                       # 이동하는 방의 개수
i = 1                           # 벌집의 개수를 세주기 위한 변수
a = 1                           # 생성되는 벌집의 개수를 세주기 위한 변수

while True:
    if (n - a) <= 0:        # N이 현재까지 누적된 벌집보다 작거나 같은 경우
        break
    n -= a                  # n에서 현재 누적된 벌집을 빼줌
    a = 6 * i               # 다음 생성되는 벌집의 개수
    i += 1
    count += 1              # 이동하는 방

print(count)