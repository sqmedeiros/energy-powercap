from collections import defaultdict,Counter,deque
import math
import bisect
from itertools import accumulate, product
from math import ceil, log,gcd
from functools import lru_cache
from sys import stdin, stdout
import time
import atexit
import io
import sys
import string
import heapq
import copy
import random
import bisect

def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]



def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    stdout.write(sep.join(str(a) for a in args) + end)

def read():
    return stdin.readline().rstrip()


def primes_rwh(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def prime_factors(n):
    i = 2
    factors = []
    d = defaultdict(lambda:0)
    for i in primes_rwh(int(n**0.5+1)):
        while  n % i == 0:
                n //= i
                factors.append(i)
                d[i]+=1
    if n > 1:
        factors.append(n)
        d[n]+=1
    return factors,d



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm    


# def bitsoncount(i):
#     assert 0 <= i < 0x100000000
#     i = i - ((i >> 1) & 0x55555555)
#     i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
#     return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24   
def bitsoncount(x): 
      b=0
      while(x > 0):
          x &= x - 1   
          b+=1
      return b
def prime_factors_s(n):
    i = 2
    factors =set()
    d = defaultdict(lambda:0)
    for i in primes_rwh(int(n**0.5+1)):
        while  n % i == 0:
                n //= i
                factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

from bisect import    bisect_right 


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return math.gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = math.gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = math.gcd(abs(x - y), n)
                if f != n:
                    return f
    return n    

def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__

@memodict
def prime_factors_r(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors_r(f) + prime_factors_r(n // f)

def multiply(a, b):

    # Creating an auxiliary matrix
    # to store elements of the
    # multiplication matrix
    mul = [[0 for x in range(2)]
              for y in range(2)];
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mul[i][j] += a[i][k] * b[k][j];
            mul[i][j] %= (10**9+7 )   
    return mul


def power(F, n):
    # print(n)
    # Multiply it with initial values i.e
    # with F(0) = 0, F(1) = 1, F(2) = 1
    if (n == 1):
        return F

    F_ = power(F, int(n // 2));

    F_ = multiply(F_, F_);

    if (n % 2 != 0):
        F_ = multiply(F_, F);

    # Multiply it with initial values i.e
    # with F(0) = 0, F(1) = 1, F(2) = 1
    return F_ ;


from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))
def calc_primes(n):
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
            179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
            283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
            419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
            547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
            661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
            811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
            947, 953, 967, 971, 977, 983, 991, 997]
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
            179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
            283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
            419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
            547 ]

@lru_cache(None)
def factorize(n):
    factorization = set()
    for d in p:
        if d * d > n:
            break
        while n % d == 0:
            factorization.add(d)
            n //= d
    if n > 1:
        factorization.add(n)
    return sorted(factorization)


@lru_cache(None)
def factorize_full(n):
    factorization = set()
    for d in p:
        if d * d > n:
            break
        c = 1
        while n % d == 0:
            factorization.add(d**c)
            n //= d
            c+=1
    if n > 1:
        factorization.add(n)
    return sorted(factorization)

def z(s):
    n = len(s)
    ret = [0] * n
    l = 1
    ll = 0
    r = 0
    while l < len(s):
        # print(l,ll,r,ret)
        if l < r:
            ret[l] = min(ret[l-ll],r-l)

        i = ret[l]
        # print(l,s[l:],i)    
        while l+i < len(s) and s[i] == s[l+i]:
            ret[l] +=1

            i +=1
        if ret[l] >0:
            if l+i-1 > r:
                ll = l
                r = max(r,l+i-1)        
        l+=1
    return ret

# def primes(n):
#     if n<=2:
#         return []
#     sieve=[set() for i in range(n+1)]
#     for x in p:
#         for y in range(1,(n//x)+1,1):
#             sieve[(x*y)].add(x)
#             # sieve[(x*y)].add(n//x)
#     return [*map(list,sieve)]

def powm(x, n, m):
    if (n ==0):
        return 1
    elif (n==1):
        return x%m

    t = powm(x,n//2,m)
    t = t * t

    if (n%2==1):
        t *= x

    t%=m
    if (t <0):
        t +=m
    return t



def z(s):
    n = len(s)
    ret = [0] * n
    l = 1
    ll = 0
    r = 0
    while l < len(s):
        # print(l,ll,r,ret)
        if l < r:
            ret[l] = min(ret[l-ll],r-l)

        i = ret[l]
        # print(l,s[l:],i)    
        while l+i < len(s) and s[i] == s[l+i]:
            ret[l] +=1

            i +=1
        if ret[l] >0:
            if l+i-1 > r:
                ll = l
                r = max(r,l+i-1)        
        l+=1
    return ret

import random as rd
class SET():
    def init(self):
        self.R = rd.randint(1<<30, 1<<60)
        self.S = set()

    def IN(self,x):
        if x^self.R in self.S:
            return True
        else:
            return False

    def add(self, x):
        self.S.add(self.R^x)

    def erase(self,x):
        if self.IN(x):
            self.S.remove(self.R^x)

# total = int(read())
# n,k = [*map(int, read().split(' '))]
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

from hashlib import sha256

#Li Chao
class Node:
    def __init__(self):
        self.k=10**18
        self.t = 10**18
        self.L, self.R=-10,10**7
        self.left = None
        self.right = None

def UpdateHelper(curr, k_new, t_new):
    f = lambda x,k,t: k*x+t


    print(k_new,t_new,curr.L,curr.R)
    m = curr.L + (curr.R-curr.L) // 2+1
    # print(curr.L,curr.R, m)
    lef = f(curr.L,curr.k,curr.t) > f(curr.L,k_new,t_new)
    mid = f(m,curr.k,curr.t) > f(m,k_new,t_new)
    print(lef,mid)
    if mid :
        tmp = k_new, t_new
        k_new, t_new = curr.k,curr.t
        curr.k,curr.t = tmp

    if curr.R == curr.L:
        return 

    # If the index is in the left subtree
    if (lef != mid) :
        print('go left')
        # Create a new node if the left
        # subtree is None
        if (curr.left == None):
            curr.left = Node()
            curr.left.L = curr.L
            curr.left.R = m-1
            curr.left.k = k_new
            curr.left.t = t_new



        # Recursively call the function
        # for the left subtree
        else:
            # print(curr.left.L, curr.left.R)
            UpdateHelper(curr.left, k_new, t_new)


    # If the index is in the right subtree
    else :
        print('go right')
        # Create a new node if the right
        # subtree is None
        if (curr.right == None):
            curr.right = Node()
            curr.right.L = m
            curr.right.R = curr.R
            curr.right.k = k_new
            curr.right.t = t_new


        # Recursively call the function
        # for the right subtree
        else:
            # print(curr.right.L, curr.right.R)
            UpdateHelper(curr.right, k_new, t_new)


    return


# Function to find the sum of the
# values given by the range
def queryHelper(curr, x):

    # Return 0 if the root is None
    if (curr == None):
        return 10**18

    m = curr.L + (curr.R-curr.L) // 2+1
    if curr.R == curr.L:
        return curr.k*x + curr.t
    elif (x < m):
        return min(curr.k*x + curr.t, queryHelper(curr.left,x))
    else:
        return min(curr.k*x + curr.t, queryHelper(curr.right,x))


def pow( x,  n, m):
    if (n ==0):
        return 1;
    elif (n==1):
        return x%m;

    t = pow(x,n//2,m);
    t = t * t;

    if (n%2==1):
        t *= x;

    t%=m;
    if (t <0):
        t +=m;
    return t;
import itertools
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# n,x = [*map(int, read().split(' '))]

# s =  [*map(int, read().split(' '))]
# f =  [*map(int, read().split(' '))]



# a = [0, 1, 19, 271, 3439, 40951, 468559, 5217031, 56953279, 612579511, 6513215599, 68618940391, 717570463519, 7458134171671, 77123207545039, 794108867905351, 8146979811148159, 83322818300333431, 849905364703000879, 8649148282327007911, 87842334540943071199]

# def c4(n):
#     if (n < 4):
#         return 0
#     d = int(math.log10(n))
#     p = math.ceil(10**d)
#     msb = n // p
#     if (msb == 4):
#         return (msb) * a[d] + (n % p) + 1
#     if (msb > 4):
#         return ((msb - 1) * a[d] + p +
#                  c4(n % p))
#     return (msb) * a[d] + c4(n % p)



# def f(x):
#     return x - c4(x)

# 


# total = int(read())
# total = 10000
total = 1

# mod = 998244353
mod = 1000000007
# pow2 = [1]

# for i in range(1,10**7+10):
#     pow2.append((pow2[-1]*2)%mod  )

# pow3 = [1]

# for i in range(1,10**7+10):
#     pow3.append((pow3[-1]*3)%mod  )

# pow4m = [1]

# mlt = pow(4, mod-2,mod)

# for i in range(1,10**7+10):
#     pow4m.append((pow4m[-1]*mlt)%mod  )

# pow34 = [1]

# mlt = (3*pow(4, mod-2,mod))%mod

# for i in range(1,10**7+10):
#     pow34.append((pow34[-1]*mlt)%mod  )




for _ in range(total):
    # n = int(read())
    # n  = 8
    # s = read()

    n,x = [*map(int, read().split(' '))]

    # a = [*map(int, read().split(' '))]
    # n = 3

    c =  [*map(int, read().split(' '))]


    dp = [0] * (x+max(c)+10)
    dp[0] = 1


    for i in range(x+1):
        for j in c:
                dp[i+j] +=dp[i]
                dp[i+j]%=mod    


    print(dp[x] if dp[x] < 10**17 else -1) 