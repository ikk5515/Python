# BOJ_15904_UCPC는_무엇의_약자일까?

str = input()

ucpc = ['U', 'C', 'P', 'C']
count = 0

for i in range(4):
    if ucpc[i] in str:                  # 만약 문자열에 'U' 'C' 'P' 'C'가 각각 있으면
        count += 1
        index = str.find(ucpc[i])       # 문자열이 있는 위치를 찾고
        str = str[index+1:]            # 인덱스 슬라이싱으로 그 다음 위치부터 끝까지 다시 찾음
    else:
        print("I hate UCPC")
        break

if count == 4:
    print("I love UCPC")

