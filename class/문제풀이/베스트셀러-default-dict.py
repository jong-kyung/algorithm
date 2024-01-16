from collections import defaultdict

# 파이썬 딕셔너리의 정렬 우선 순위
# 1. value
# 2. key
# 딕셔너리는 sort 메서드는 사용이 안되지만 sorted는 사용이 가능하다.

books_sales_info = defaultdict(int)

for _ in range(int(input())):
    books_sales_info[input().rstrip()] += 1 # 키값 선언 없이 바로 연산

# 키 람다를 이용한 정렬
# sorted(books_sales_info.items(), key=lambda x:(-x[1],x[0])) # 첫번째 인자를 우선순위로 정렬후 두번째 인자를 다음 순위로 정렬함

# for문을 통한 정렬
books_names = sorted(books_sales_info)

cnt = -1
ans = ''

for book_name in books_names:
    if books_sales_info[book_name] > cnt:
        cnt = books_sales_info[book_name]
        ans = book_name

print(ans)