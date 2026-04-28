import sys
sys.setrecursionlimit(10**6)

def dfs(u, graph, subordinates):
    count = 0
    for v in graph[u]:
        count += 1 + dfs(v, graph, subordinates)
    subordinates[u] = count
    return count

def main():
    input = sys.stdin.readline
    n = int(input())
    bosses = list(map(int, input().split()))

    # Build adjacency list: boss -> list of direct reports
    graph = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        boss = bosses[i - 2]
        graph[boss].append(i)

    subordinates = [0] * (n + 1)
    dfs(1, graph, subordinates)

    print(' '.join(str(subordinates[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()