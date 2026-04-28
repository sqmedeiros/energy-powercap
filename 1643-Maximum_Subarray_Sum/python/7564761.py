# Problem: Maximum Subarray Sum
# Contest: CSES - CSES Problem Set
# URL: https://cses.fi/problemset/task/1643
# Memory Limit: 512 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)


# created by NARZULLAYEV SAIDMUROD
import bisect
import random

mod = 10 ** 9 + 7
eps = 10 ** -9

def _miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2;

        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False;

def _isprime(n):
    if (n < 2 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1;
    while (d % 2 == 0):
        d //= 2
    for i in range(5):
        if (_miillerTest(d, n) == False):
            return False

    return True

def _gcd(a, b):
    return a if b == 0 else _gcd(b, a % b)


def _lcm(a, b):
  return a * b // _gcd(a, b)

def _mex(a):
    mex = 0
    a.sort()
    for x in a:
        if x <= mex:
            mex += 1
        else:
            break
    return mex

def _dist(x1, y1, x2, y2):
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

def _getprimes(n, m):
    primes = []
    if n <= 2:
        primes.append(2)
    if n % 2 == 0:
        n += 1
    for i in range(n, m + 1, 2):
        if _isprime(i):
            primes.append(i)
    return primes

def _primefactors(n):
    ret = []
    x = n
    i = 2
    if _isprime(n):
        ret.append(n)
        return ret
    while i * i <= x:
        while n % i == 0:      
            ret.append(i)
            n //= i
            if _isprime(n):
                break
        i += 1
    if n > 1:
        ret.append(n)
    return ret

def _pollardrho(n):
    if n % 2 == 0: return 2
    if _isprime(n): return n
    while True:
        c = random.randint(2, n -1)
        f = lambda x: x**2 + c 
        x = y = 2 
        d = 1 
        while d == 1:
            x = f(x) % n 
            y = f(f(y)) % n 
            d = _gcd((x - y) % n, n)

        if d != n and _isprime(d): return d

def _sumdigit(n):
  ret = 0
  while n > 0:
    ret += n % 10
    n //= 10
  return ret

def _modinverse(n, m):
    return (n % mod) * (pow(m, mod - 2, mod) % mod) % mod

def p(n):
 return print(n, end = ' ')
def lip(type = int):
 return list(map(type, input().split()))

def mip(type = int):
 return map(type, input().split())

def tip(type = int):
 return type(input())

def inp():
 return input()
yes = 'YES'
no = 'NO' 
def solve(t):

 n = tip()
 a = lip()
 ans = a[0]
 cnt = 0
 for i in a:
  cnt = max(i, cnt + i)
  ans = max(ans, cnt)
 print(ans)
t = 1
# t = int(input())
for i in range(t):
    solve(i + 1)