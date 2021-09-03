naver_closing_price = [474500, 461500, 501000, 500500, 488500]

max_price = max(naver_closing_price)
min_price = min(naver_closing_price)

print(max_price)
print(min_price)

print('가격차: ',max_price - min_price)

print('수요일 종가: ', naver_closing_price[2])

naver_closing_price2 = {'09/07': 474500, '09/08': 461500, '09/09': 501000, '09/10': 500500,
 '09/11': 488500}
print(naver_closing_price2)

print(naver_closing_price2['09/09'])
