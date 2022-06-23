#BOJ_2751_수_정렬하기2
from sys import stdin

n = stdin.readline()
arr = []


for i in range(int(n)):
    arr.append((int(input())))

arr.sort()

for i in range(int(n)):
    print(arr[i])
