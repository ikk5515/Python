myinfo = {}

myinfo['name'] = "김인기"
myinfo['age'] = 23  # 키-값 추가
myinfo['age'] = 24  # 키-값 수정

myinfo['height'] = 163.2  # 키-값 추가

del myinfo['height']  # 키-값 삭제

print(f"내 이름은 {myinfo['name']}입니다.")
# print(f"내 키는{myinfo['height']}입니다.")

height = myinfo.get('height')
if height == None:
    print("아직 키 정보가 입력되지 않았습니다.")
else:
    print(f"내 키는{'height'}cm입니다.")