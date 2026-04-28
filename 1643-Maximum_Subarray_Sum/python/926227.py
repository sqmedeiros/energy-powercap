def solve(n,a):
    INF = 1000000000
    dp = n*[-INF]

    dp[0] = a[0]
    for idx in range(1,n):
        dp[idx] = max(a[idx], dp[idx-1]+a[idx])

    # print(dp)
    return max(dp)


def main():
    n = int(input())
    a = [int(x) for x in input().split(' ')]

    print(solve(n,a))

if __name__ == "__main__":
    main()