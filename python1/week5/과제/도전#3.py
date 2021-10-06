students = []
total = 0
avg = 0
for i in range(5):
    all_students = dict()
    all_students['name'] = input('이름 : ')
    all_students['score'] = int(input('성적 입력 : '))
    total += all_students['score']
    avg = total / 5
    students.append(all_students)


print("이 름    성적")
for i in range(len(students)):
    student = students[i]
    print(f"{student['name']} \t{student['score']}")

print(f"총 평균: {avg}")
