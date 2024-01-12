N = int(input())

for num in range(1, N+1):
    disassemble = num + sum(map(int, str(num)))

    if disassemble == N:
        print(num)
        break

else:
    print(0)