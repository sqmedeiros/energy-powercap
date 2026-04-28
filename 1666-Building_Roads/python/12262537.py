import sys
import random
import math
import collections

input = sys.stdin.readline
output = sys.stdout.write


# sys.setrecursionlimit(110000)
# input = sys.stdin.read
# data = input().split()
def I(): return int(input())


def S(): return input().strip()


def F(): return float(input())


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def MF(): return map(float, input().split())


def LMI(): return list(map(int, input().split()))


def LMS(): return list(map(str, input().split()))


def LMF(): return list(map(float, input().split()))


def OA(arr): return output(" ".join(map(str, arr)) + "\n")


def ON(n): return output(str(n) + "\n")


def yes():
    output("YES\n")


def no():
    output("NO\n")
MOD = 998244353
MOD1 = 10 ** 9 + 7

def adjm(inp, n):
    adj = [[] for _ in range(n)]

    for line in inp:
        no1, no2 = line
        adj[no1 - 1].append(no2 - 1)
        adj[no2 - 1].append(no1 - 1)

    return adj

n, m = LMI()
inp = [LMI() for i in range(m)]
AL = adjm(inp, n)
visited = [False] * n

def dfs(r, AL):
    visited[r] = True
    stack = collections.deque([(r,-1)])
    while stack:
        r, c = stack.pop()
        for child in AL[r]:
            if not visited[child]:
                stack.append((child,r))
                visited[child] = True


rooms = 0
results = []
last = 1
for i in range(n):
    if not visited[i]:
        rooms += 1
        if rooms > 1:
            results.append([last, i + 1])
        last = i + 1
        dfs(i, AL)

ON(rooms - 1)
for line in results:
    print(" ".join(map(str,line)))












































