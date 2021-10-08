def build_profile(first, last, **userinfo):
    print(f"{last}{first}의 추가정보는 아래와 같습니다.")
    print(f"   활동지역 : {userinfo.get('loc', '정보없음')}")
    print(f"   전공분야 : {userinfo.get('field', '정보없음')}")
    print(f"   기사타항:  {userinfo.get('etc',)}")


build_profile('albert', 'einstein', loc='princeton')
build_profile(last='kim', first='inha', loc='incheon', field='cs')
build_profile('inha', 'lee', loc='incheon', field='lg')
build_profile(first='inha', loc='incheon', last='kim', field='cs')