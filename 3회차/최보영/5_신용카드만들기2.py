import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_nums = list(map(int, input().replace('-', '')))
    
    res = 0
    if card_nums[0] == 3 or card_nums[0] == 4 or card_nums[0] == 5 or card_nums[0] == 6 or card_nums[0] == 9:
        if len(card_nums) == 16:
            res = 1
    
    print(f'#{test_case} {res}')