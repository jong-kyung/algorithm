# SWEA 문제해결 기본 구간합

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 최초값 설정
    max_sum, min_sum = 0, 987654321

    for i in range(N-M+1):
        # 슬라이싱 통해 구간합 구하기
        cnt = sum(nums[i:i+M])

        # 최대값 및 최소값 갱신
        max_sum = max(cnt, max_sum)
        min_sum = min(cnt, min_sum)

    print(f'#{tc} {max_sum - min_sum}')