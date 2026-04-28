# لا تَجلِس فارِغًا [ حرك لسانك ]
# اسْتَغفِر ، سَبّح ، هَلّل ، كَبّر ، حَولق

import sys
from random import randint, shuffle, choice
from math import gcd, sqrt, isqrt, perm, log, comb, factorial, log2, ceil, floor
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product, repeat, takewhile, starmap, dropwhile, cycle
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush, _heapify_max
from bisect import bisect_left, bisect_right, insort_left, insort_right
#from operator import sub, mul, pow, truediv, floordiv
input = lambda: sys.stdin.buffer.readline().decode().rstrip()
OneByOne = lambda: sys.stdin.read(1)

def lcm(a, b):
    return a * b // gcd(a, b)
def W(i):
    return (i, str(i))

def MakeFile(s: str, r='in', v='out'):
    import sys
    sys.stdin = open(f'{s}.{r}', 'r')
    sys.stdout = open(f'{r}.{v}', 'w')

#def is_valid(x, y): # Grid
#    return 0 <= x < n and 0 <= y < m and \
#        graph[x][y] != '#' and not vis[x][y]

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
yes = lambda: print('YES')
no = lambda: print('NO')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIR4 = (((-1), 0), (0, 1), (1, 0), (0, (-1)))
DIR8 = (((-1), 0), ((-1), 1), (0, 1), (1, 1), (1, 0), (1, (-1)), (0, (-1)), ((-1), (-1)))
DIR4_prime = [((-1), 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, (-1), 'L')]
MOD = 10 ** 9 + 7
inf = float('inf')

#!فَالعَينُ عانِيَةٌ تَفيضُ دُموعُها
#!لِمَنازِلٍ دَرَسَت كَأَن لَم تُؤهَلِ

#!دارٌ لِقَومٍ قَد أَراهُم مَرَّةً
#!فَوقَ الأَعِزَّةِ عِزُّهُم لَم يُنقَلِ

#!لِلَّهِ دَرُّ عِصابَةٍ نادَمتُهُم
#!يَوماً بِجِلَّقَ في الزَمانِ الأَوَّلِ

#!نَسَبي أَصيلٌ في الكِرامِ وَمِذوَدي
#!تَكوي مَواسِمُهُ جُنوبَ المُصطَلي

#!وَلَقَد تُقَلِّدُنا العَشيرَةُ أَمرَها
#!وَنَسودُ يَومَ النائِباتِ وَنَعتَلي


#for _ in range(II()):

MAXN = 10**6

fac = [0] * (MAXN + 1)
inv = [0] * (MAXN + 1)


def exp(x: int, n: int, m: int) -> int:
  """:return: x^n modulo m in O(log p) time."""
  x %= m  # note: m * m must be less than 2^63 to avoid ll overflow
  res = 1
  while n > 0:
    if n % 2 == 1:
      res = (res * x) % m
    x = (x * x) % m
    n //= 2
  return res


def factorial(p: int):
  """Precomputes n! from 0 to MAXN."""
  global fac
  fac[0] = 1
  for i in range(1, MAXN + 1):
    fac[i] = (fac[i - 1] * i) % p


def inverses(p: int):
  """
  Precomputes all modular inverse factorials from 0 to MAXN in O(n + log p) time
  """
  global inv
  inv[MAXN] = exp(fac[MAXN], p - 2, p)
  for i in range(MAXN, 0, (-1)):
    inv[i - 1] = (inv[i] * i) % p


def choose(n: int, r: int, p: int):
  """:return: nCr mod p"""
  return fac[n] * inv[r] % p * inv[n - r] % p


n , k = MII()
a = LII()
ans = 0
for i in range(1 , 1 << k) :
    now = 1
    ss = 0 
    for j in range(k) :
        if ((1 << j) & i) :
            now *= a[j] 
            ss += 1 
            if now > n : 
                break

    if now > n : continue
    ans -= ((-1) ** ss) * (n // now)

print(ans)