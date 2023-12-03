# SWEA 문제해결 기본 min max

T = int(input()) # test case 숫자

for tc in range(1, T+1):
    N = int(input()) # 입력값 갯수
    nums = list(map(int, input().split())) # 입력값 받기
    answer = max(nums) - min(nums) # 정답
    print(f'#{tc} {answer}')