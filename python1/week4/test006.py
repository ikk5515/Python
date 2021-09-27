numbers = input("4자리의 정수 입력: ")  #numbers = "1234"

# numbers_int = [ int(n) for n in numbers ]   #[1,2,3,4]

# 리스트( 0 ~ n-1), 문자열( 0 ~ n-1)

numbers_int = list(map(int, numbers))

print(sum(numbers_int))
