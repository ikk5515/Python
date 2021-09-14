insert = int(input("투입한 돈: "))
price = int(input("물건의 가격: "))
change = insert - price
print(f"거스름 돈: {change}")
fivehund = change // 500
rest = change % 500
onehund = rest // 100
print(f"500 동전 개수: {fivehund}")
print(f"100 동전 개수: {onehund}")
