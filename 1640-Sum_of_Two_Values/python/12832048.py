n, x = map(int, input().split())

a = [*map(int, input().split())]
s = sorted(range(n), key=lambda x: a[x])

i = 0
j = n - 1

while i != j:
    current = a[s[i]] + a[s[j]]
    if current > x:
        j -= 1
    if current < x:
        i += 1
    if current == x:
        break

if i == j:
    print("IMPOSSIBLE")
else:
    print(s[i] + 1, s[j] + 1)