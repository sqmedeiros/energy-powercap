# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
# CodeChef  : https://www.codechef.com/users/majay1638
from sunau import Au_read
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def Solution(graph, n, m):
    # Write Your Code Here
    queue = [1]
    ans = []
    vis = [False]*(n+1)
    vis[1] = True
    par = [i for i in range(n+1)]
    while len(queue):
        node = queue.pop(0)
        if node == n:
            break
        for child in graph[node]:
            if vis[child]:
                continue
            par[child] = node
            vis[child] = True
            queue.append(child)
    curr = n
    flg = True
    while curr != 1:
        if par[curr] == curr:
            flg = False
            break
        ans.append(curr)
        curr = par[curr]
    # print(par, "sdfd")
    ans.append(curr)
    if flg:
        print(len(ans))
        print(*list(reversed(ans)))
    else:
        print("IMPOSSIBLE")


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = get_ints_in_variables()
        graph[v].append(u)
        graph[u].append(v)
    Solution(graph, n, m)


# calling main Function
if __name__ == '__main__':
    main()