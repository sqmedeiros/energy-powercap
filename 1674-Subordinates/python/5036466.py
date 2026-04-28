#!/usr/bin/env python3

from collections import Counter, deque


def main():
    n = int(input())
    direct_bosses = [0, 0] + [int(x) for x in input().strip().split()]
    in_degs = Counter(direct_bosses)
    q = deque(set(range(2, n+1)) - set(direct_bosses))
    subordinates = [0]*(n+1)

    while q:
        x = q.popleft()
        boss = direct_bosses[x]
        subordinates[boss] += subordinates[x]+1

        if boss == 1:
            continue

        if (in_degs[boss] == 1):
            q.append(boss)
        in_degs[boss] -= 1


    print(" ".join(str(x) for x in subordinates[1:]))


if __name__ == "__main__":
    main()