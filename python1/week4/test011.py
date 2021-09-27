req_topping = ['버섯', '양파']

if req_topping:                     # 리스트가 비어있으면 False, 1개 이상이라도 있으면 True
    for topping in req_topping:
        if topping == '페퍼로니':
            print("재고가 소진됐어요, 페퍼로니가 없어요.")
        else:
            print(f"{topping} 추가")

    print("피자완성!")
else:
    print("모든 재고 소진!")
