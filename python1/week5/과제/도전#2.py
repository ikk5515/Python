favorite_books = {
    '정재승의 과학 콘서트': {'name': '정재승', 'publisher': '어크로스', 'pub_year': '2020.07.07'},
    '위대한 개츠비': {'name': '리처드 도킨스', 'publisher': '을유문화사', 'pub_year': '2018.10.20'},
    '침묵의 봄': {'name': '레이첼 카슨', 'publisher': '에코리브르', 'pub_year': '2011.12.30'}
}

for number, book in favorite_books.items():
    print(f"책 제목: {number}")
    print(f"작가: {book['name']}")
    print(f"출판사: {book['publisher']}")
    print(f"출판년도: {book['pub_year']}\n")
