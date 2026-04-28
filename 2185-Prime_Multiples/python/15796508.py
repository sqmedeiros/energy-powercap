def solve():
    # Input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    # Iterate over all subsets using bitmasking (from 1 to 2^k - 1)
    for i in range(1, 1 << k):
        prod = 1
        cnt = -1
        for j in range(k):
            if (i & (1 << j)) != 0:  # Check if the j-th bit is set
                # Check for overflow, avoid multiplying if prod would exceed n
                if prod > n // a[j]:
                    prod = n + 1
                    break
                prod *= a[j]
                cnt *= -1  # Flip the sign for inclusion-exclusion

        if prod <= n:
            ans += cnt * (n // prod)

    print(ans)

# Driver code to run the function
if __name__ == "__main__":
    solve()