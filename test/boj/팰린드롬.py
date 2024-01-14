for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            word = words[i] + words[j]

            if word == word[::-1]:
                print(word)
                exit(0)

    print(0)