"""
For God so loved the world that he gave his one and only Son, 
that whoever believes in him shall not perish but have eternal life.
JOHN 3:16 
"""
#imports
import random
from math import *
from functools import lru_cache,cmp_to_key
from itertools import *
from fractions import Fraction
from bisect import bisect_left as bl
from bisect import bisect_right as br
from operator import itemgetter
from collections import Counter,deque,defaultdict
from heapq import heappop as hpop, heappush as hpush
YES = ['NO','YES']
Yes = ["No","Yes"]
yes = ["no","yes"]
# constants
MOD = [10**9 + 7,998244353]
MOD = MOD[0]
rand = random.randint(10**8,10**9)
n,m,files = 0,0,0
import sys
if files:sys.stdin = open("input.txt");sys.stdout = open("output.txt", 'w')
input = sys.stdin.readline
output = sys.stdout.write
#sys.setrecursionlimit(110000)
# #For large input
# input = sys.stdin.read
# data = input().split()
# Shortcut for input()
def I(): return int(input())
def S(): return input().strip()
def F(): return float(input())
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def MF(): return map(float,input().split())
def LI(): return list(MI())
def LS(): return list(MS())
def LF(): return list(MF())
def MAT(n): return [LI() for _ in range(n)]
#fast_pow,add,sub,pro -works well when p is prime or composite
def fast_pow(a, b, n):  # a^b % n using binary exponentiation
    a %= n
    res = 1
    while b:
        if b & 1:
            res = res * a % n
        a = a * a % n
        b >>= 1
    return res
def add(a, b): return (a % MOD + b % MOD) % MOD
def sub(a, b): return (a % MOD - b % MOD + MOD) % MOD
def pro(a, b): return (a % MOD * b % MOD) % MOD
# Division using inverse: valid only when inv(b) exists (gcd(b, MOD) = 1)
def div(a, b): return pro(a, inv(b))
# Inverse assuming MOD is prime
def inv(a): return fast_pow(a, MOD - 2, MOD)
# Extended Euclidean Algorithm (works for any MOD if gcd(a, MOD) == 1)
def invcom(a):
    def egcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = egcd(b, a % b)
        return g, y1, x1 - (a // b) * y1
    g, x, _ = egcd(a, MOD)
    return (x % MOD) if g == 1 else "no solution"
def inbound(i,j): return 0 <= i < n and 0 <= j < m
def idx(i,j):return i*m + j # DSU [2D - 1D] (0 - n*m-1)
def idxs(n): return [n//m,n%m] #DSU [2D - 1D] 
def summ(n):return (n * (n+1))>>1
def nc2(n):return summ(n-1)
def sod(n): return sum(int(i) for i in str(n))
def cdc(n):return (10*n-sod(n))//9
DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]
DIR8 = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
direction = {(-1,0):"U",(1,0):"D",(0,-1):"L",(0,1):"R"}
direction_reverse = {"L":(0,1),"R":(0,-1),"U":(1,0),"D":(-1,0)}
#Shortcut for output()
res = []
def OI(res): output("\n".join(res))
def OL(res): output("\n".join(" ".join(i) for i in res))


"""
 """

# CSES — Round Trip (iterative DFS / stack-based)
import sys
from collections import defaultdict

def find_cycle_iterative(n, edges):
    adj = [[] for _ in range(n+1)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)

    state = [0]*(n+1)   # 0=unvisited,1=processing,2=done
    parent = [-1]*(n+1)

    for s in range(1, n+1):
        if state[s] != 0:
            continue
        # stack items: (node, parent, next_index)
        stack = [(s, -1, 0)]
        while stack:
            u, p, idx = stack[-1]
            if idx == 0:
                state[u] = 1
                parent[u] = p

            if idx < len(adj[u]):
                v = adj[u][idx]
                # increment next_index
                stack[-1] = (u, p, idx+1)

                if v == p:
                    # skip the immediate parent edge in undirected graph
                    continue

                if state[v] == 0:
                    # go deeper
                    stack.append((v, u, 0))
                elif state[v] == 1:
                    # found a back-edge -> cycle from v .. u .. v
                    cycle = [v]
                    cur = u
                    while cur != v:
                        cycle.append(cur)
                        cur = parent[cur]
                    cycle.append(v)  # repeat start to close cycle
                    return cycle
                # if state[v] == 2 -> ignore (cross/tree edge already processed)
            else:
                # finished all neighbours
                stack.pop()
                state[u] = 2

    return None

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    cycle = find_cycle_iterative(n, edges)
    if not cycle:
        print("IMPOSSIBLE")
    else:
        print(len(cycle))
        print(*cycle)

if __name__ == "__main__":
    main()