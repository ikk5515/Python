motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw', 'ducati', 'vespa']

findindex = motorcycles.index('suzuki')
print(findindex)

# 인덱스 삭제
del motorcycles[findindex]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

if len(motorcycles) > 11:
    del motorcycles[10]
    print(motorcycles)
else:
    print("10 인덱스가 없어요")

del motorcycles[:2]
print(motorcycles)

