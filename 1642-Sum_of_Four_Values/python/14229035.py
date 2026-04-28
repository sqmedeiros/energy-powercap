from collections import defaultdict

def find_four_sum_indices(n, x, arr):
    # Dictionary to store pair sums
    pair_sum = defaultdict(list)

    # Iterate over all pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum[arr[i] + arr[j]].append((i + 1, j + 1))  # Store 1-based indices

    # Iterate over all pairs (k, l)
    for k in range(n):
        for l in range(k + 1, n):
            target = x - (arr[k] + arr[l])
            if target in pair_sum:
                for (i, j) in pair_sum[target]:
                    # Ensure all indices are distinct
                    if i != k + 1 and i != l + 1 and j != k + 1 and j != l + 1:
                        return i, j, k + 1, l + 1

    return "IMPOSSIBLE"

# Input reading
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Function call and output
result = find_four_sum_indices(n, x, arr)
if result == "IMPOSSIBLE":
    print(result)
else:
    print(*result)