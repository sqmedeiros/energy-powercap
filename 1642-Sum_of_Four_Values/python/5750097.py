# 3
# 13, half = 6
# 2 3 8

# 2 3 4 8
# 17, half = 8
#                    |        |                     
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# 2 4 6 8
# 20
# 8
from collections import defaultdict

def solve():
    _, target = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    d = defaultdict(list)
    for i, num1 in enumerate(nums):
        for j in range(i+1, len(nums)):
            d[num1+nums[j]].append((i+1, j+1))

    for key, pairs in d.items():
        another = d.get(target - key)
        if another and (2*key != target or len(another) > 1):
            a, b, c, e = pairs[0][0], pairs[0][1], another[-1][0], another[-1][1]
            if len({a,b,c,e}) == 4:
                return f'{a} {b} {c} {e}'
    return 'IMPOSSIBLE'

print(solve())