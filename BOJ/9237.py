#BOJ_9237_이장님_초
n = int(input())
arr = []

arr = list(map(int, input().split()))

arr.sort(reverse=True)

for i in range(len(arr)):
    arr[i] = arr[i] + i + 1;

print(max(arr) + 1)