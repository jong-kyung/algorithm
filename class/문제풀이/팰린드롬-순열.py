import sys
from itertools import permutations

input = sys.stdin.readline

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for word1, word2 in permutations(words, 2):
        p = word1 + word2

        if p == p[::-1]:
            print(p)
            exit(0) # break를 이용하면 가장 가까운 for문만 멈추기 때문에 exit을 통해 하나만 찾은 이후 파이썬파일을 강제 종료함.

    print(0)