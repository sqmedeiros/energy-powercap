import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()

ans = [-1]*(k+1)
ans[0] = 0

for i in range(1, k+1):
    for j in range(n):
        cur = a[j]
        if cur <= i:
            prev = ans[i-cur]
            if prev == -1:
                continue
            if ans[i] == -1:
                ans[i] = prev + 1
            else:
                ans[i] = min(ans[i], prev + 1)
        else:
            break

print(ans[-1])