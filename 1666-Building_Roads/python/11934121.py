"""
@file: building_roads.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Building Roads(https://cses.fi/problemset/task/1666)
@version: 1.0
@date: 2025-01-31
 @copyright: Copyright (c) 2025
"""

from collections import defaultdict, deque
from sys import stdin, stdout
from types import GeneratorType


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


# pajenegod orz
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def main():
    n, m = [int(x) for x in input().split()]
    adj = defaultdict(list)
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    c = [0] * (n + 1)

    for i in range(1, n + 1):
        if not c[i]:
            stack = deque([i])
            c[i] = i
            while stack:
                node = stack.pop()
                for neighbor in adj[node]:
                    if not c[neighbor]:
                        c[neighbor] = i
                        stack.append(neighbor)

    cs = sorted(set(c))
    print(len(cs) - 2)
    for i in range(2, len(cs)):
        print(f"{cs[1]} {cs[i]}")


if __name__ == "__main__":
    main()