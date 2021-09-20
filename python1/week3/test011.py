values = [1, 2, 3, 4, 5, 6, 7]


max = int(input("최대수: "))
values = []
for value in range(1, max):
    values.append(value)

print(values)

values = [v for v in range(1,max)]
print(values)

values = [v**2 for v in range(1, max)]
print(values)

values = [v**2 for v in range(1, max) if v % 2 == 0]
print(values)
