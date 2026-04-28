import sys
input = sys.stdin.readline

n, target = map(int, input().split())
vals = list(map(int, input().split()))

pair_map = {}

for i in range(n):
    for j in range(i + 1, n):
        curr_sum = vals[i] + vals[j]
        need_sum = target - curr_sum

        if need_sum in pair_map:
            for x, y in pair_map[need_sum]:
                if x != i and x != j and y != i and y != j:
                    print(x + 1, y + 1, i + 1, j + 1)
                    sys.exit(0)

        if curr_sum not in pair_map:
            pair_map[curr_sum] = []
        pair_map[curr_sum].append((i, j))

print("IMPOSSIBLE")