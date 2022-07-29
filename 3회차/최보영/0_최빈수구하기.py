import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for _ in range(T):
    test_case = int(input())
    
    scores = list(map(int, input().split()))
    s_dict = dict()

    for s in scores:
        s_dict[s] = s_dict.get(s, 0) + 1

    # 최빈수 내림차 → 점수 내림차
    res = sorted(s_dict.items(), key=lambda x: (-x[1], -x[0]))
    
    print(f'#{test_case} {res[0][0]}')