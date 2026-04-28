import sys
input = sys.stdin.readline

rn = lambda: int(input())
rs = lambda: input().strip()
rl = lambda: list(map(int, input().split()))
def _print(*args):
    sys.stdout.write('\033[94m>> \033[35m' + ' '.join(map(str, args)) + '\033[0m\n')

from itertools import combinations as c
from math import prod as p

def solve():
    n,k = rl()
    s = rl()
    print(sum([-1,1][i&1]*sum(n//p(x) for x in c(s,i)) for i in range(1,k+1)))

solve()