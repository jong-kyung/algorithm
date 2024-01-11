total = int(input())
books = {}

# 저장할 수 있는 배열을 만들면 좋을듯? 딕셔너리 자료형으로
for i in range(total): # 자료 받기
    title = input()

    if title not in books:
        books[title] = 1
    else:
        books[title] += 1
# 가장 큰 밸류를 가진아이를 출력
maxCount = max(books.values())

best = []

for key, value in books.items():
    if value == maxCount:
        best.append(key)

best = sorted(best)
print(best[0])