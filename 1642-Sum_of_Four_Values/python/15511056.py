n, x = map(int, input().split())
arr = list(map(int, input().split()))


pair_sum = {}

for i in range(n):
    for j in range(i + 1, n):
        s = arr[i] + arr[j]
        need = x - s


        if need in pair_sum:
            a, b = pair_sum[need]
            # Ensure all indices are distinct
            if a != i and a != j and b != i and b != j:
                # Output 1-based indices
                print(a + 1, b + 1, i + 1, j + 1)
                exit()


        if s not in pair_sum:
            pair_sum[s] = (i, j)

print("IMPOSSIBLE")