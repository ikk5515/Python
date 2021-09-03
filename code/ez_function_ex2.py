def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)  # 리스트도 사용 가능

(upper, lower) = cal_upper_lower(10000)

print(cal_upper_lower(10000))

print(upper)

print(lower)