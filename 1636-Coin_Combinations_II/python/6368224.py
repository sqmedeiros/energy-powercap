n, x = map(int, input().split())
c = [int(i) for i in input().split()]
f = [1] + [0]*x
for u in c:
    for i in range(1, x+1):
        if i - u >= 0:
            f[i] = (f[i] + f[i-u]) % 1000000007
print(f[x])