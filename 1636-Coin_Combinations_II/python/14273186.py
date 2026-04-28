import sys

DEBUG = False
MOD = 10**9 + 7

def debug(*args, **kwargs):
    """Prints debug info only when DEBUG is True."""
    if DEBUG:
        print(*args, **kwargs,file = sys.stderr)

def get_factors(N):
    factors = set()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(N // i)
    return sorted(factors)



# def bottom up approach
def solve(sum,coins):
    dp = [0] * (sum+1)
    dp[0] = 1

    for coin in coins:
        for s in range(coin,sum+1):
            if s - coin >= 0:
                dp[s] = (dp[s] + dp[s-coin])%MOD

    return dp[sum]


def main():

    input_data = sys.stdin.read().strip().split()
    index = 0
    out = []

    t = 1
    #index += 1

    for _ in range(t):
        n = int(input_data[index])
        index += 1
        sum = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index + n]))
        index += n
        out.append(str(solve(sum,arr)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()