avl_topping = ['버섯', '피망', '치즈', '올리브', '양파', '페퍼로니']
req_topping = ['버섯', '양파', '파인애플', '페퍼로니']

for req in req_topping:
    if req in avl_topping:
        print(f"{req} 토핑 추가!")
    else:
        print(f"{req} 토핑은 재고가 없습니다. ")

print("피자 완성!")
