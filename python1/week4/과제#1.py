people = int(input("명수: "))
pizza_amount = int(input("피자주문수량: "))
pizza_piece = int(input("조각: "))


person_piece = (pizza_amount * pizza_piece) // people
pizza_remain = (pizza_amount * pizza_piece) % people
print(f"인당 {person_piece} 조각, 남은 피자는 {pizza_remain} 조각")