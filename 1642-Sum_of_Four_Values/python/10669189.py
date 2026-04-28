def find_four_sum(arr, x):
    n = len(arr)
    pair_sum = {}  # Dictionary to store sum of pairs

    for i in range(n):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            if current_sum not in pair_sum:
                pair_sum[current_sum] = []
            pair_sum[current_sum].append((i, j))

    for sum1 in pair_sum:
        sum2 = x - sum1  # We need to find another pair that sums to x - sum1
        if sum2 in pair_sum:
            for pair1 in pair_sum[sum1]:
                for pair2 in pair_sum[sum2]:
                    i, j = pair1
                    k, l = pair2

                    # Ensure all indices are distinct
                    if i != k and i != l and j != k and j != l:
                        # Found the solution
                        return [i+1, j+1, k+1, l+1]

    return None  # No solution found

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = find_four_sum(arr, k)
if result:
    print(*result)
else:
    print("IMPOSSIBLE")