n, x = map(int, input().split())
m = list(map(int, input().split()))
mp = {}  # sum -> list of pairs
for i in range(n):
    for j in range(i + 1, n):
        s = m[i] + m[j]
        need = x - s
        if need in mp:
            for p, q in mp[need]:
                if p != i and p != j and q != i and q != j:
                    print(p+1, q+1, i+1, j+1)
                    exit()
        if s not in mp:
            mp[s] = []
        mp[s].append((i, j))
print("IMPOSSIBLE")