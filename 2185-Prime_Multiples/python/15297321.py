import sys
sys.setrecursionlimit(10**6)

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    k = int(data[1])
    primes = list(map(int, data[2:]))

    ans = 0

    # DFS over subsets: try including primes[j] for j >= i
    # sign: +1 for odd-sized subset (adds), -1 for even-sized subset (subtracts)
    def dfs(i, prod, sign):
        nonlocal ans
        for j in range(i, k):
            new = prod * primes[j]
            if new > n:
                # since primes aren't guaranteed sorted, we cannot break;
                # but skipping is enough (pruning)
                continue
            ans += sign * (n // new)
            dfs(j + 1, new, -sign)

    dfs(0, 1, 1)
    print(ans)

if __name__ == "__main__":
    main()