n, t = map(int, input().split())
arr = list(map(int, input().split()))
mp = {}

for i in range(n):
    for j in range(i + 1, n):
        sm = arr[i] + arr[j]
        need = t - sm
        if need in mp:
            x, y = mp[need]
            if x != i and x != j and y != i and y != j:
                print(x + 1, y + 1, i + 1, j + 1)
                exit()
        mp.setdefault(sm, (i, j))

print("IMPOSSIBLE")