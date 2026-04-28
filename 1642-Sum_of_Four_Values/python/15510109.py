import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

pairs = {}

for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        need = x - s
        if need in pairs:
            for p, q in pairs[need]:
                if p != i and p != j and q != i and q != j:
                    print(p+1, q+1, i+1, j+1)
                    sys.exit(0)
        if s not in pairs:
            pairs[s] = []
        pairs[s].append((i, j))

print("IMPOSSIBLE")