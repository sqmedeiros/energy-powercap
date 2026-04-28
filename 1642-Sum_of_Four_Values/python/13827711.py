def four_sum_indices(n, x, arr):
    from collections import defaultdict

    pair_sum = defaultdict(list)

    # Store all possible pair sums with their indices
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            pair_sum[s].append((i, j))

    # Try to find two non-overlapping pairs that sum to x
    for s in pair_sum:
        complement = x - s
        if complement not in pair_sum:
            continue

        # Try all combinations of pairs from s and complement
        for i1, j1 in pair_sum[s]:
            for i2, j2 in pair_sum[complement]:
                # Make sure all indices are unique
                if len(set([i1, j1, i2, j2])) == 4:
                    # Return 1-based indices
                    return f"{i1+1} {j1+1} {i2+1} {j2+1}"

    return "IMPOSSIBLE"


# Input reading
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Solve and print result
print(four_sum_indices(n, x, arr))