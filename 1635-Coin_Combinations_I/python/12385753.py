# Money Sums

n,x = map(int, input().split())
c = list(map(int, input().split()))

memo = [0] * (x+1)
memo[0] = 1
mod = (10**9) + 7

for i in range(min(c),x+1):
    for coin in c:
        if coin <= i:
            memo[i] += memo[i-coin]
    memo[i] %= mod
print(memo[x])
