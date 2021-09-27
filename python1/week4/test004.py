#4자리의 정수를 받는다.
#문자열 -> 정수 형 변환

#4번째, 3번쨰, 2번째, 1번째 각 자리별 숫자를 뽑는다.
# // , %
#각 자리수의 합을 계산하고 출력한다.

numbers = int(input("4자리의 정수 입력: "))
#"1234" => 1234
# 1 + 2 + 3 + 4 = 10

n4 = numbers // 1000    # 1 234//1000 = 1 (/를 쓰면 소수점이 생김)
numbers = numbers % 1000    # 1234 % 1000 = 234

n3 = numbers // 100     # 234 // 100 = 2
numbers = numbers % 100   # 234 % 100 = 34

n2 = numbers // 10       # 34 // 10 = 3
numbers = numbers % 10    # 34 % 10 = 4

n1 = numbers // 1         # 4 / 1 = 4
numbers = numbers % 1     # 4 % 1 = 0

result = n4 + n3 + n2 + n1
print(result)
