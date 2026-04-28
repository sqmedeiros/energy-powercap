import sys
sys.setrecursionlimit(10**7)

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])

    # Build adjacency list (children list)
    adj = [[] for _ in range(n + 1)]

    idx = 1
    for emp in range(2, n + 1):
        boss = int(data[idx])
        idx += 1
        adj[boss].append(emp)

    sub = [0] * (n + 1)

    def dfs(u):
        count = 0
        for v in adj[u]:
            count += 1 + dfs(v)
        sub[u] = count
        return count

    dfs(1)

    # Print results for employees 1...n
    print(*sub[1:])

if __name__ == "__main__":
    main()