s5 = {1, 2, 3}
s5.add(44)
s5.add(1)  # 기존에 1이란 값이 있으므로 무시된다.
print(s5)

s5.update([4, 5, 6])
print(s5)

s5.update("1234")
print(s5)

s5.remove(1)
print(s5)

s5.remove('1')
print(s5)