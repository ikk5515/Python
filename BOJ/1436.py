N = int(input())
count = 0

for i in range(100000000):
    if '666' in str(i):
        count += 1
        if count == N:
            print(str(i))
            break


