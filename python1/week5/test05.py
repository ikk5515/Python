print("1~10 사이의 숫자 중 홀수의 합")

count = 0
sum = 0

while count < 10:
    count += 1
    if count % 2 != 0:
        # pass 빈 블록
        sum += count

print(sum)
