import sys
from math import gcd, factorial as fact,hypot,acos,atan2,pi,ceil,sqrt,log2,isqrt,log,dist,perm,comb,prod,exp
try: from math import lcm
except: lcm = lambda a,b: a//gcd(a,b)*b
from heapq import *
from itertools import *
try:
 from functools import cache
except:
 from functools import lru_cache
 def cache(user_function, /):
  return lru_cache(maxsize=None)(user_function)
from functools import reduce, cmp_to_key
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
from fractions import Fraction as frac
import typing
import operator
try:
 from tqdm import trange
except:
 trange = range

# import pypyjit
# pypyjit.set_param(max_unroll_recursion=-1,vec=1)
sys.setrecursionlimit(10**5+10)

input = lambda: sys.stdin.readline().strip()
def read(fn=int):
 return map(fn,input().split())
def read(*fn):
 if not fn: fn = [int]
 l = input().split()
 if len(fn) == 1: return map(fn[0], l)
 return (f(x) for f,x in zip(fn,l))

def dbg(*args,**kwargs):
 print(*args,**kwargs,file=sys.stderr)

class ostream():
 def __lshift__(self,s):
  sys.stdout.write(str(s))
  return self
cout = ostream()
endl = '\n'

yes = 'YES'
no = 'NO'

# toks = (tok for tok in sys.stdin.read().split())
# def rd(fn=int): return fn(next(toks))
# def rdn(n,fn=int): return (rd(fn) for _ in range(n))

mod = 998244353
mod = 10**9 + 7

def mul(a,b,mod=0):
 if sum(map(sum,a)) == 0 or sum(map(sum,b)) == 0:
  return [[0]*len(b[0]) for _ in range(len(a))]
 c = [[0 for j in range(len(b[0]))] for i in range(len(a))]
 for i in range(len(a)):
  for k in range(len(b)):
   for j in range(len(b[0])):
    c[i][j] += a[i][k]*b[k][j]
    if mod: c[i][j] %= mod
 return c

def power(x,y,mod=0):
 n = len(x)
 res = [[+(i==j) for j in range(n)] for i in range(n)]
 while y:
  if y % 2: res = mul(res,x,mod)
  x = mul(x,x,mod)
  y //= 2
 return res 

def sieve(n):
 primes = []
 isp = [1] * (n+1)
 isp[0] = isp[1] = 0
 for i in range(2,n+1):
  if isp[i]:
   primes += [i]
   for j in range(i*i,n+1,i):
    isp[j] = 0
 return primes

def eea(a,b):
 if not a: return b,0,1
 g,x,y = eea(b%a,a)
 return g, y - (b//a)*x, x

def factorials(n,mod):
 facs = [1 % mod]
 for i in range(n):
  facs += [facs[-1] * (i+1) % mod]
 invs = [pow(facs[-1], -1, mod)]
 for i in range(n):
  invs += [invs[-1] * (n-i) % mod]
 invs.reverse()
 return facs, invs

def _ceil_pow2(n):
 x = 0
 while (1 << x) < n:
  x += 1

 return x

def _bsf(n):
 x = 0
 while n % 2 == 0:
  x += 1
  n //= 2

 return x

class FenwickTree:
 def __init__(self, n = 0):
  self._n = n
  self.data = [0] * n

 def add(self, p, x):
  assert 0 <= p < self._n

  p += 1
  while p <= self._n:
   self.data[p - 1] += x
   p += p & -p

 def sum(self, left, right):
  assert 0 <= left <= right <= self._n

  return self._sum(right) - self._sum(left)

 def _sum(self, r: int):
  s = 0
  while r > 0:
   s += self.data[r - 1]
   r -= r & -r

  return s

class SegTree:
 def __init__(self,
     op: typing.Callable[[typing.Any, typing.Any], typing.Any],
     e: typing.Any,
     v: typing.Union[int, typing.List[typing.Any]]) -> None:
  self._op = op
  self._e = e

  if isinstance(v, int):
   v = [e] * v

  self._n = len(v)
  self._log = _ceil_pow2(self._n)
  self._size = 1 << self._log
  self._d = [e] * (2 * self._size)

  for i in range(self._n):
   self._d[self._size + i] = v[i]
  for i in range(self._size - 1, 0, -1):
   self._update(i)

 def set(self, p: int, x: typing.Any) -> None:
  assert 0 <= p < self._n

  p += self._size
  self._d[p] = x
  for i in range(1, self._log + 1):
   self._update(p >> i)

 def get(self, p: int) -> typing.Any:
  assert 0 <= p < self._n

  return self._d[p + self._size]

 def prod(self, left: int, right: int) -> typing.Any:
  assert 0 <= left <= right <= self._n
  sml = self._e
  smr = self._e
  left += self._size
  right += self._size

  while left < right:
   if left & 1:
    sml = self._op(sml, self._d[left])
    left += 1
   if right & 1:
    right -= 1
    smr = self._op(self._d[right], smr)
   left >>= 1
   right >>= 1

  return self._op(sml, smr)

 def all_prod(self) -> typing.Any:
  return self._d[1]

 def max_right(self, left: int,
      f: typing.Callable[[typing.Any], bool]) -> int:
  assert 0 <= left <= self._n
  assert f(self._e)

  if left == self._n:
   return self._n

  left += self._size
  sm = self._e

  first = True
  while first or (left & -left) != left:
   first = False
   while left % 2 == 0:
    left >>= 1
   if not f(self._op(sm, self._d[left])):
    while left < self._size:
     left *= 2
     if f(self._op(sm, self._d[left])):
      sm = self._op(sm, self._d[left])
      left += 1
    return left - self._size
   sm = self._op(sm, self._d[left])
   left += 1

  return self._n

 def min_left(self, right: int,
     f: typing.Callable[[typing.Any], bool]) -> int:
  assert 0 <= right <= self._n
  assert f(self._e)

  if right == 0:
   return 0

  right += self._size
  sm = self._e

  first = True
  while first or (right & -right) != right:
   first = False
   right -= 1
   while right > 1 and right % 2:
    right >>= 1
   if not f(self._op(self._d[right], sm)):
    while right < self._size:
     right = 2 * right + 1
     if f(self._op(self._d[right], sm)):
      sm = self._op(self._d[right], sm)
      right -= 1
    return right + 1 - self._size
   sm = self._op(self._d[right], sm)

  return 0

 def _update(self, k: int) -> None:
  self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

class LazySegTree:
 def __init__(
   self,
   op: typing.Callable[[typing.Any, typing.Any], typing.Any],
   e: typing.Any,
   mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
   composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
   id_: typing.Any,
   v: typing.Union[int, typing.List[typing.Any]]) -> None:
  self._op = op
  self._e = e
  self._mapping = mapping
  self._composition = composition
  self._id = id_

  if isinstance(v, int):
   v = [e] * v

  self._n = len(v)
  self._log = _ceil_pow2(self._n)
  self._size = 1 << self._log
  self._d = [e] * (2 * self._size)
  self._lz = [self._id] * self._size
  for i in range(self._n):
   self._d[self._size + i] = v[i]
  for i in range(self._size - 1, 0, -1):
   self._update(i)

 def set(self, p: int, x: typing.Any) -> None:
  assert 0 <= p < self._n

  p += self._size
  for i in range(self._log, 0, -1):
   self._push(p >> i)
  self._d[p] = x
  for i in range(1, self._log + 1):
   self._update(p >> i)

 def get(self, p: int) -> typing.Any:
  assert 0 <= p < self._n

  p += self._size
  for i in range(self._log, 0, -1):
   self._push(p >> i)
  return self._d[p]

 def prod(self, left: int, right: int) -> typing.Any:
  assert 0 <= left <= right <= self._n

  if left == right:
   return self._e

  left += self._size
  right += self._size

  for i in range(self._log, 0, -1):
   if ((left >> i) << i) != left:
    self._push(left >> i)
   if ((right >> i) << i) != right:
    self._push(right >> i)

  sml = self._e
  smr = self._e
  while left < right:
   if left & 1:
    sml = self._op(sml, self._d[left])
    left += 1
   if right & 1:
    right -= 1
    smr = self._op(self._d[right], smr)
   left >>= 1
   right >>= 1

  return self._op(sml, smr)

 def all_prod(self) -> typing.Any:
  return self._d[1]

 def apply(self, left: int, right: typing.Optional[int] = None,
     f: typing.Optional[typing.Any] = None) -> None:
  assert f is not None

  if right is None:
   p = left
   assert 0 <= left < self._n

   p += self._size
   for i in range(self._log, 0, -1):
    self._push(p >> i)
   self._d[p] = self._mapping(f, self._d[p])
   for i in range(1, self._log + 1):
    self._update(p >> i)
  else:
   assert 0 <= left <= right <= self._n
   if left == right:
    return

   left += self._size
   right += self._size

   for i in range(self._log, 0, -1):
    if ((left >> i) << i) != left:
     self._push(left >> i)
    if ((right >> i) << i) != right:
     self._push((right - 1) >> i)

   l2 = left
   r2 = right
   while left < right:
    if left & 1:
     self._all_apply(left, f)
     left += 1
    if right & 1:
     right -= 1
     self._all_apply(right, f)
    left >>= 1
    right >>= 1
   left = l2
   right = r2

   for i in range(1, self._log + 1):
    if ((left >> i) << i) != left:
     self._update(left >> i)
    if ((right >> i) << i) != right:
     self._update((right - 1) >> i)

 def max_right(
   self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
  assert 0 <= left <= self._n
  assert g(self._e)

  if left == self._n:
   return self._n

  left += self._size
  for i in range(self._log, 0, -1):
   self._push(left >> i)

  sm = self._e
  first = True
  while first or (left & -left) != left:
   first = False
   while left % 2 == 0:
    left >>= 1
   if not g(self._op(sm, self._d[left])):
    while left < self._size:
     self._push(left)
     left *= 2
     if g(self._op(sm, self._d[left])):
      sm = self._op(sm, self._d[left])
      left += 1
    return left - self._size
   sm = self._op(sm, self._d[left])
   left += 1

  return self._n

 def min_left(self, right: int, g: typing.Any) -> int:
  assert 0 <= right <= self._n
  assert g(self._e)

  if right == 0:
   return 0

  right += self._size
  for i in range(self._log, 0, -1):
   self._push((right - 1) >> i)

  sm = self._e
  first = True
  while first or (right & -right) != right:
   first = False
   right -= 1
   while right > 1 and right % 2:
    right >>= 1
   if not g(self._op(self._d[right], sm)):
    while right < self._size:
     self._push(right)
     right = 2 * right + 1
     if g(self._op(self._d[right], sm)):
      sm = self._op(self._d[right], sm)
      right -= 1
    return right + 1 - self._size
   sm = self._op(self._d[right], sm)

  return 0

 def _update(self, k: int) -> None:
  self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

 def _all_apply(self, k: int, f: typing.Any) -> None:
  self._d[k] = self._mapping(f, self._d[k])
  if k < self._size:
   self._lz[k] = self._composition(f, self._lz[k])

 def _push(self, k: int) -> None:
  self._all_apply(2 * k, self._lz[k])
  self._all_apply(2 * k + 1, self._lz[k])
  self._lz[k] = self._id

def solve2(case):
 q,w=read()
 l = [[*read()] for _ in range(q)]
 s={0}
 for i in range(q):
  x,y=l[i]
  l[i]=[max(x-y,0), min(x+y,w)]
  s |= {*l[i]}
 s=sorted(s)
 # print(s)
 d = {s[i]:i for i in range(len(s))}
 val = [0] * len(s)
 for i in range(len(s)-1):
  val[i] = s[i+1] - s[i]
 val[-1] = w - s[-1]
 # print(s,val)
 n = len(s)
 sz = isqrt(n)
 # print(n,sz,(n+sz-1)//sz)
 b = [0] * ((n+sz-1)//sz)
 # print(len(b), max(y//sz for _,y in l))
 f = [Counter() for _ in range((n+sz-1)//sz)]
 for i in range(len(s)):
  f[i//sz][0] += val[i]
 a = [0]*n
 seen = set()
 ans = w
 for x,y in l:
  x = d[x]
  y = d[y]
  # print(x,y)
  if (x,y) in seen:
   delta = -1
   seen.remove((x,y))
  else:
   delta = 1
   seen.add((x,y))

  bx = x // sz
  by = y // sz
  # print(bx,by)
  if bx == by:
   ans -= f[bx][-b[bx]]
   for i in range(x,y):
    f[bx][a[i]] -= val[i]
    a[i] += delta
    f[bx][a[i]] += val[i]
   ans += f[bx][-b[bx]]
  else:
   ans -= f[bx][-b[bx]]
   for i in range(x,(x+sz)//sz*sz):
    f[bx][a[i]] -= val[i]
    a[i] += delta
    f[bx][a[i]] += val[i]
   ans += f[bx][-b[bx]]

   ans -= f[by][-b[by]]
   for i in range(y//sz*sz,y):
    f[by][a[i]] -= val[i]
    a[i] += delta
    f[by][a[i]] += val[i]
   ans += f[by][-b[by]]

   for i in range(bx+1,by):
    ans -= f[i][-b[i]]
    b[i] += delta
    ans += f[i][-b[i]]

  # print(x,y)
  # print(bx,by)
  # print(delta)
  # print(b)
  # print(a)
  # print(f)
  # print(ans)
  print((w-ans) * 2**.5)
  # print()

def solve2(case):
 adj = []
 pre = []
 res = []
 order = []
 order_rev = []
 def ar_build(el):
  for _ in range(n):
   adj.append([])
   pre.append([])
   res.append(False)
  for i,(x,y) in enumerate(el):
   adj[x].append((y,i))
   adj[y].append((x,i))

 def ar_down(x, p=-1):
  # val = False
  # for y,ei in adj[x]:
  #  if y != p:
  #   val = val | ar_down(y,x)
  #   pre[x].append(val)
  # return not val

  for x,p in order:
   val = False
   for y,_ in adj[x]:
    if y != p:
     val = val | (not pre[y][-1] if pre[y] else True)
     pre[x].append(val)

 def ar_up(x,p=-1):
  adj[x].reverse()
  for y,ei in adj[x]:
   if y == p: continue
   if pre[x]: pre[x].pop()
   res[y] = not ((res[x] or pre[x][-1]) if pre[x] else res[x])
   res[x] = res[x] or not (pre[y][-1] if pre[y] else False)
   ar_up(y,x)
  res[x] = not res[x]

  # for x,p in order_rev:


 def calc(el):
  ar_build(el)
  order.append((0,-1))
  order_rev.append((0,-1))
  vis = [0] * n
  vis_rev = [0] * n
  ptr = 0
  while ptr < len(order):
   v,p = order[ptr]
   vis[v] = 1
   for vv,_ in adj[v]:
    if not vis[vv]:
     order.append((vv,v))

   v,p = order_rev[ptr]
   vis_rev[v] = 1
   for vv,_ in reversed(adj[v]):
    if not vis_rev[vv]:
     order_rev.append((vv,v))

   ptr += 1
  order.reverse()
  order_rev.reverse()
  print(order)
  ar_down(0)
  ar_up(0)

 n,q = read()
 el = []
 for _ in range(n-1):
  x,y=read()
  el.append((x-1,y-1))

 calc(el)

 for x in read():
  print('Hermione' if res[x-1] else 'Ron')

def matmul(a,b,mod=0):
 c = [[0]*len(b[0]) for i in range(len(a))]
 for i in range(len(a)):
  for k in range(len(b)):
   for j in range(len(b[0])):
    c[i][j] += a[i][k]*b[k][j]
    if mod: c[i][j] %= mod
 return c

# def comb(x,y):
#  (x0,),(x1,),(x2,) = x
#  (y0,),(y1,),(y2,) = y
#  return [[(x1+x2)*(y1+y2)], [(x0+y0+x0*y2+x2*y0)], [(x0*y1 + x1*y0)]]

# def solve(case):
#  for m in range(3**9):
#   l = []
#   for _ in range(9):
#    l+=[m%3]
#    m//=3
#   l.reverse()
#   a,b,c,d,e,f,g,h,i = l

#   T = [[a,b,c],[d,e,f],[g,h,i]]
#   for v in range(3**6):
#    x,y = divmod(v,3**3)
#    xa,xb,xc = x//9, x//3%3, x%3
#    X = [[xa],[xb],[xc]]
#    ya,yb,yc = y//9, y//3%3, y%3
#    Y = [[ya],[yb],[yc]]

#    XY = comb(X,Y)
#    TXY = matmul(T,XY)
#    TX = matmul(T,X)
#    TY = matmul(T,Y)
#    if TXY != comb(TX,TY):
#     break
#   else:
#    print(T)

def comb(x,y):
 (x0,x1,x2), = x
 (y0,y1,y2), = y
 return [[(x1+x2)*(y1+y2), x0*y0+x0*y2+x2*y0, x0*y1+x1*y0]]

def solve2(case):
 # for m in trange(5**9):
 #  l = []
 #  for _ in range(9):
 #   l+=[m%5-2]
 #   m//=5
 #  l.reverse()
 #  a,b,c,d,e,f,g,h,i = l
 #  if a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h == 0: continue

 #  T = [[a,b,c],[d,e,f],[g,h,i]]
 #  for v in range(3**6):
 #   x,y = divmod(v,3**3)
 #   xa,xb,xc = x//9, x//3%3, x%3
 #   X = [[xa, xb, xc]]
 #   ya,yb,yc = y//9, y//3%3, y%3
 #   Y = [[ya, yb, yc]]

 #   V1 = matmul(comb(X,Y),T)[0]
 #   TX = matmul(X,T)[0]
 #   TY = matmul(Y,T)[0]
 #   V2 = [TX[0] * TY[0], TX[1] * TY[1], TX[2] * TY[2]]
 #   if V1 != V2:
 #    break
 #  else:
 #   print(T)


 n,k = read()
 events = []
 ranges = []
 for i in range(n):
  a,b=read()
  events.append([a,-1,i])
  events.append([b,1,i])
  ranges.append([a,b])
 events.sort()
 # print(events)
 mx = 0
 c = 0
 pv = -1
 for x,f,i in events:
  if f == 1:
   c -= 1
   if pv != -1:
    mx = max(mx, x-pv+1)
   if c < k:
    pv = -1
  else:
   c += 1
   if pv == -1 and c >= k:
    pv = x
 # print(mx)
 if mx == 0:
  print(0)
  print(*range(1,k+1))
  return

 c = 0
 pv = -1
 active = set()
 for x,f,i in events:
  if f == 1:
   c -= 1
   if pv != -1 and x-pv+1 == mx:
    print(mx)
    # print(*sorted(active)[:k])
    l = sorted(active,key=lambda x:ranges[x-1][0])
    print(*l[:k])
    return
   if c < k:
    pv = -1
   active.remove(i+1)
  else:
   c += 1
   active.add(i+1)
   if pv == -1 and c == k:
    pv = x

def solve(case):
 n,=read()
 l=[*read()]
 adj=[[]for _ in range(n)]
 for i in range(1,n):
  p=l[i-1]-1
  adj[i]+=[p]
  adj[p]+=[i]
 bfs=[0]
 seen=[0]*n
 seen[0]=1
 for v in bfs:
  for vv in adj[v]:
   if not seen[vv]:
    seen[vv]=1
    bfs.append(vv)
 bfs.reverse()
 bfs.pop()
 sz=[0]*n
 for v in bfs:
  sz[l[v-1]-1]+=sz[v]+1
 print(*sz)


if __name__ == '__main__':
 t = 1
 # t = -1
 # t, = read()
 for i in range(1,t+1):
  solve(i)
  t -= 1