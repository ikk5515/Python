# BOJ_1350_진짜_공간
import math
import sys

result = 0
arr = []
N = int(sys.stdin.readline())

arr = (list(map(int, input().split())))

a = int(sys.stdin.readline())

for i in range(N):
    if arr[i] == 0:
        continue
    if arr[i] <= a:
        result += a
    if arr[i] > a:
        arr[i] = arr[i] / a
        result += a * math.ceil(arr[i])

print(result)
