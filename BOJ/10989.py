#BOJ_10989_수_정렬하기3
import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):                      # 리스트 0부터 인덱스를 입력받고 해당 숫자가 존재하면 1씩 더해줌
    arr[int(sys.stdin.readline())] += 1

for j in range(10001):
    if arr[j] != 0:                 # 0이면 해당 숫자가 없으므로 0이 아닐 때
        for k in range(arr[j]):     # 있으면 해당 숫자만큼 반복해줌
            print(j)