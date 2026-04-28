from itertools import combinations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


for r in range(1, k+1):
    for comb in combinations(arr, r):
        pr = 1
        for num in comb:
            pr *= num

        if (r % 2):
            ans += n//pr
        else:
            ans -= n//pr


print(ans)