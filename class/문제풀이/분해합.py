import sys
input = sys.stdin.readline

N = int(input())
start = max(1, N - (9 * len(str(N)))) # 생성자의 시작 범위, 음수가 나올 수 있으므로 max를 통해 음수가 나오는 것을 방지
ans = 0

for num in range(start, N+1):
    disassemble_sum = num + sum(map(int, str(num)))

    if disassemble_sum == N:
        ans = num
        break

print(ans)