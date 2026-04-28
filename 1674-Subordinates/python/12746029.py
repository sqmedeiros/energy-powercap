import sys
from collections import deque

def solve():
    n = int(input())
    bosses = list(map(int, input().split()))


    tree = [[] for _ in range(n)]
    for i in range(n-1):
        boss = bosses[i]
        tree[boss-1].append(i+1)

    subordinate_count = [0] * n
    queue = deque([0])
    post_order = []

    while queue:
        node = queue.popleft()
        post_order.append(node)
        for subordinate in tree[node]:
            queue.append(subordinate)

    while post_order:
        node = post_order.pop()
        count = 0
        for subordinate in tree[node]:
            count += 1 + subordinate_count[subordinate]
        subordinate_count[node] = count

    sys.stdout.write(" ".join(map(str, subordinate_count)) + "\n")

solve()