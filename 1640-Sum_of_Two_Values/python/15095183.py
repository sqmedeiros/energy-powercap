import sys
input = sys.stdin.readline

def inp(): return input().strip()
def inpi(): return int(input())
def inpl(): return list(map(int, input().split()))

from collections import defaultdict

n, x = inpl()
l = inpl()
c = defaultdict(int)
for idx, i in enumerate(l):
    if i in c:
        print(c[i] + 1, idx + 1)
        break
    c[x - i] = idx
else:
    print("IMPOSSIBLE")