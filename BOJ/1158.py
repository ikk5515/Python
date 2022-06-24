# BOJ_1158_요세푸스_문제

N, K = map(int, input().split())

people = []                         # 제거된 사람들을 넣을 배열
arr = [i for i in range(1, N+1)]    # 1부터 N까지 배열에 삽입 => 원에 맨 처음 앉아있는 사람들

cnt = 0


for i in range(N):
    cnt += K -1
    if cnt >= len(arr):             # 한 바퀴를 다 돌았을 때
        cnt = cnt % len(arr)             # 길이로 나눈 나머지를 다시 대입

    people.append(str(arr.pop(cnt)))

print("<",", ".join(people)[:],">", sep = '')