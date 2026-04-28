from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    sums = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            sums[a[i] + a[j]].append((i, j))

    for i in range(n):
        for j in range(i + 1, n):
            if (k - a[i] - a[j]) in sums:
                for x, y in sums[k - a[i] - a[j]]:
                    if i != x and i != y and j != x and j != y:
                        return [i + 1, j + 1, x + 1, y + 1]

    return "IMPOSSIBLE"

ans = solve()
if ans == "IMPOSSIBLE": print(ans)
else: print(*ans)