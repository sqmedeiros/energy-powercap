from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))

# Dictionary to store sum of two elements -> list of index tuples
sum_map = defaultdict(list)

# Precompute all pairs (i, j), i < j and store their sum
for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        sum_map[s].append((i, j))

# Now try all pairs (i, j), i < j and look for complement in sum_map
for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        complement = x - s
        if complement in sum_map:
            for (p, q) in sum_map[complement]:
                # Ensure all indices are distinct
                if len({i, j, p, q}) == 4:
                    print(i+1, j+1, p+1, q+1)
                    exit()

print("IMPOSSIBLE")