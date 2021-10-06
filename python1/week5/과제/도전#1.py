favorit_places = {
    '김인하': ['부천', '인천', '여수'],
    '최컴정': ['서울', '부산'],
    '박정석': ['대전', '대구']
}

for name, places in favorit_places.items():
    print(f"{name}이(가) 좋아하는 도시는")
    for place in places:
        print(f"\t{place}")
