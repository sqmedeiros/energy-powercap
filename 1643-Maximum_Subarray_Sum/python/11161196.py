n = int(input())
a = list(map(int, input().split()))

psum = [0] * n
psum[0] = a[0]

for i in range(1, n):
    psum[i] = psum[i - 1] + a[i]

ans = psum[0]
min1 = 0

for i in psum:
    ans = max(ans, i - min1)
    min1 = min(min1, i)

print(ans)