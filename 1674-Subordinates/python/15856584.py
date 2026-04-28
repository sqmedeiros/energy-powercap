import sys
from collections import deque

def solve():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    vis = [False] * (n + 1)
    sub = [0] * (n + 1)

    arr = list(map(int, input().split()))
    for i in range (2, n + 1):
        adj[arr[i - 2]].append(i)

    q = deque([1])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            q.append(v)

    for u in reversed(order):
        for v in adj[u]:
            sub[u] += sub[v] + 1

    print(*sub[1:])



if __name__ == "__main__":
    input = sys.stdin.readline

    T = 1
    # T = int(input())
    for tt in range(1, T + 1):
        # print(f"Case {tt}: ", end="")
        solve()