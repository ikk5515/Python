#5번 반복하면서 키보드를 통해 학생의 이름을 입력 받는다.

#리스트에 저장된 학생이름 사이에 '/' 을 넣고 한꺼번에 출력한다.

names = []
for i in range(1, 6):
    names.append(input(f"{i}번 이믈: "))
    #input()을 통해서 입력받은 문자열(이름)을 리스트에 출력한다. (5번)

result = "/".join(names)

print(result)
