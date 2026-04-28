from itertools import permutations, combinations, accumulate
from collections import defaultdict, deque, Counter
from heapq import heapify, heappush, heappop, merge
from bisect import bisect_right, bisect_left
from io import StringIO,BytesIO
from math import gcd
_MOD = 998244353
MOD = 10**9 + 7
import sys,os




printf=print
input=sys.stdin.readline
defaultdictdict=defaultdict
lcm=lambda x,y:x*y//gcd(x,y)
getonestr=lambda:input().strip()
getone=lambda:int(input().strip())
getstr=lambda:list(input().split())
CEIL_DIV=lambda a,b:(a//b)+bool(a%b)
SINGLE_TESTCASE=CALL=lambda func:func()
odd=lambda N:N&1;even=lambda N:not(odd(N))
write=lambda obj:sys.stdout.write(f"{obj}")
writeln=lambda obj:sys.stdout.write(f"{obj}\n")
get=getarr=lambda:list(map(int,input().split()))
def MULTIPLE_TESTCASE(func): [func() for _ in range(getone())]
_2D_ARRAY_SPAWN=lambda i,j,T=None: [[(0 if T is None else T) for _j in range(j)] for _i in range(i)]
_3D_ARRAY_SPAWN=lambda i,j,k,T=None: [[[(0 if T is None else T) for _k in(k)] for _j in range(j)] for _i in range(i)]
rgane=rgaen=rgnae=rgnea=rgean=rgena=ragne=ragen=raneg=raegn=raeng=rngae=rngea=rnage=rnaeg=rnega=rneag=regan=regna=reagn=reang=renga=renag=range



from types import GeneratorType
def bootstrap(f, stack=[]):
    """
        ### RECURSION LIMIT BYPASS
        #### (Credits to @Pajenegod)
        Tutorial: 
        1. Treat `foo()` as a void function
        2. Do `yield foo()` for every call, yield for every return
        3. If you must return something, use a global variable and modify it instead.
        4. This can be done using a mutable object such as a list, which must exist in the same scope as the function, e.g.
        ```C++
        l = [0]
        def foo() :
            old_val = l[0]
            /* ... */
            l[0] = new_val
            yield or yield foo()
        ```
    """

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve():

        ...
        # Solution here!
        n,m = get()
        gr = defaultdict(set)
        for _ in range(m) :
                u,v = get()
                gr[u].add(v)
                gr[v].add(u)


        seen = [0] * (n + 1)
        ans = [None]
        @bootstrap
        def dfs(u, p, path) :

                if ans[0] is not None : yield
                if seen[u] :
                        if ans[0] is not None : yield
                        idx = path.index(u)
                        ans[0] = path[idx:]
                        yield
                seen[u] = 1


                for v in gr[u] :
                        if v == p : continue
                        path.append(v)
                        yield dfs(v, u, path)
                        path.pop()

                yield


        for i in range(1, n + 1) :
                if not seen[i] :
                        dfs(i, -1, [i])

                if ans[0] is not None :
                        break

        if ans[0] is None : return "IMPOSSIBLE"

        print (len(ans[0]))
        print (*ans[0])

@SINGLE_TESTCASE
def main() :
        ans = solve()
        if ans is not None: writeln(ans)