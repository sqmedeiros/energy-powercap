import sys


def main():
    # input = sys.stdin.read
    # data = input().split()
    # idx = 0
    # n = int(data[idx])
    # x = int(data[idx + 1])
    # idx += 2
    # cs = list(map(int, data[idx:idx + n]))

    n, x = map(int, input().split())
    cs = list(map(int, input().split()))

    dp = [float('inf')] * (x + 1)
    dp[0] = 0

    for i in range(x):
        if dp[i] == float('inf'):
            continue
        for c in cs:
            if i + c <= x:
                if dp[i + c] > dp[i] + 1:
                    dp[i + c] = dp[i] + 1

    print(dp[x] if dp[x] != float('inf') else -1)


if __name__ == "__main__":
    main()