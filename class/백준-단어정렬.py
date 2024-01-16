import sys
input = sys.stdin.readline # input을 한번에 받을 수 있게 하는 도구

N = int(input())

words = [input().rstrip() for _ in range(N)] # rstrip으로 개행문자(\n)를 제거

words = list(set(words))
words.sort(key=lambda x:(len(x),x))

# words.sort() # 알파벳순 정렬
# words.sort(key=lambda x:len(x)) # 길이순 정렬

for word in words:
    print(word)