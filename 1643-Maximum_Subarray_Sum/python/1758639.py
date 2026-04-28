n = int(input())
x = list(map(int, input().split()))

ans = 0
best = 0
for i in range(n):
    best = max(0, best + x[i])
    ans = max(best, ans)
if all(val < 0 for val in x):
    print(max(x))
    import sys
    sys.exit(0)
print(ans)