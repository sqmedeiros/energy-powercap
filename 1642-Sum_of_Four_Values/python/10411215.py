from collections import defaultdict

N, X = map(int, input().split())
a = list(map(int, input().split()))

mp = defaultdict(list)

for i in range(1, N):
    for j in range(i):
        psum = a[i] + a[j]
        if psum >= X:
            continue
        if (X - psum) in mp:
            for p in mp[X - psum]:
                if p[0] != j and p[1] != j and p[0] != i and p[1] != i:
                    print(p[0] + 1, p[1] + 1, j + 1, i + 1)
                    exit(0)
        mp[psum].append((j, i))

print("IMPOSSIBLE")