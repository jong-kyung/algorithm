def func(n):
    if n == 3:
        return

    print(f'{n}의 세상에 옴')
    func(n+1)
    print(f'{n}의 세상의 마무리')

func(0)

# 재귀 함수 = 시스템 스택이 생김을 의미한다. 즉 후입선출형의 자료구조이다.