def find(i):
    if dsu[i] < 0:
        return i
    else:
        dsu[i] = find(dsu[i])
        return dsu[i]

def join(i, j):
    i = find(i)
    j = find(j)
    if i == j:
        return False
    if dsu[i] > dsu[j]:
        dsu[i] = j
    else:
        if dsu[i] == dsu[j]:
            dsu[i] -= 1
        dsu[j] = i
    return True

n, m = map(int, input().split())
dsu = [-1] * n
k = n-1
while m:
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if join(a, b):
        k -= 1
    m -= 1 
print(k)
r = -1
for i, v in enumerate(dsu):
    if v < 0:
        if r != -1:
            print(r+1, i+1)
        r = i 