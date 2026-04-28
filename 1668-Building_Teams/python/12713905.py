from collections import defaultdict
import sys

def res(friends):
    next_group = {"1": "2", "2": "1"}
    output = [""] * (n + 1)
    for i in range(1, n + 1):
        if output[i] == "":
            q = [(i, "1")]
        while q:
            child, group = q.pop()
            forbidden = friends[child]
            if output[child] != "":
                if output[child] != group:
                    return "IMPOSSIBLE"
            output[child] = group
            q.extend([(f, next_group[group]) for f in forbidden if output[f] == ""])

    return " ".join(output[1:])

n, m = map(int, sys.stdin.readline().split())

friends = defaultdict(set)
connected = defaultdict(set)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].add(b)
    friends[b].add(a)

print(res(friends))