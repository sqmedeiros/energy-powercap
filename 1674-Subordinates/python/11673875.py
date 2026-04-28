import sys
from collections import defaultdict


def count_subordinates(n, bosses):
    sys.setrecursionlimit(1 << 25)

    tree = defaultdict(list)
    for employee, boss in enumerate(bosses, start=2):
        tree[boss].append(employee)

    count = [0] * (n + 1)

    def dfs(employee):
        for subordinate in tree[employee]:
            count[employee] += 1 + dfs(subordinate)
        return count[employee]

    dfs(1)
    return count[1:]


if __name__ == "__main__":
    n = int(input())
    bosses = list(map(int, input().split()))
    print(*count_subordinates(n, bosses))