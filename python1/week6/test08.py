def describe_pet(type, name='아직미정'):
    print(f"나는 {type}(이)라는 동물을 데리고 있어요.")
    print(f"내 {type}의 이름은 {name}입니다. ")


describe_pet('햄스터', '해리')
describe_pet(type='새', name='카나리아')
describe_pet(name='방울이', type='개')
describe_pet('뱀', name='돌돌이')
# describe_pet(name='캬악', '사마귀')    # 실행 안됨
describe_pet('코끼리')