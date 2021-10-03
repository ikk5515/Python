s0 = {1, 2, 3, 3, 4, 5}
s1 = {1, 4, 4, 4, 5, 6, 7, 7, 10}

# 합집합 - union
union1 = s0 | s1
union2 = s0.union(s1)
print(union1)
print(union2)

# 교집합 - intersection
intersction1 = s0 & s1
intersction2 = s0.intersection(s1)
print(intersction1)
print(intersction2)

# 차집합 - difference

dif1 = s0 - s1
dif2 = s1.difference(s0)
print(dif1)
print(dif2)