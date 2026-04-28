n,x = map(int, input().split())
a = list(map(int, input().split()))


mod = (10**9)+7

m = [0]*(x+1)
m[0] = 1


for d in a:
    for i in range(d, x+1):
       m[i] = (m[i] + m[i - d]) % mod

print(m[x])