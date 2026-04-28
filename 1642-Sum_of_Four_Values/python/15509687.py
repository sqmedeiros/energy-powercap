n, x = map(int, input().split())
a = list(map(int, input().split()))

# Dictionary to store sum of two numbers -> their indices
pair_sum = {}

for i in range(n):
    for j in range(i + 1, n):
        current = a[i] + a[j]
        required = x - current

        # Check if required sum already exists
        if required in pair_sum:
            p, q = pair_sum[required]
            # Ensure all indices are distinct
            if p != i and p != j and q != i and q != j:
                print(p + 1, q + 1, i + 1, j + 1)
                exit()

    # Store previous pairs
    for k in range(i):
        pair_sum[a[k] + a[i]] = (k, i)

print("IMPOSSIBLE")