MOD = 10**9 + 7

n, x = map(int, input().split())
c = list(map(int, input().split()))
tab=[0] * (x + 1)
tab[0] = 1
for j in c:
    for i in range(j, x+1):
        if j <= i:
            tab[i] = (tab[i] + tab[i - j]) % MOD
print(tab[x])