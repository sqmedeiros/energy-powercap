import sys
input = sys.stdin.readline

n,x = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

memo = [int(1e9)]*(1+x)
memo[0] = 0
for i in range(1, x+1):
    for coin in c:
        if i - coin >= 0:
            memo[i] = min(memo[i], memo[i-coin]+1)
        else:
            break

print(memo[x] if memo[x] != int(1e9) else -1)