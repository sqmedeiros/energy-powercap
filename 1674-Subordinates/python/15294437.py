import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    bosses = [next(it) for _ in range(n - 1)]

    adj = [[] for _ in range(n + 1)]
    for i, b in enumerate(bosses, start=2):
        adj[b].append(i)

    stack = [1]
    order = []   
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            stack.append(v)

    sub = [0] * (n + 1)
    for u in reversed(order):
        total = 0
        for v in adj[u]:
            total += sub[v] + 1
        sub[u] = total

    out = " ".join(str(sub[i]) for i in range(1, n + 1))
    sys.stdout.write(out)

if __name__ == "__main__":
    main()