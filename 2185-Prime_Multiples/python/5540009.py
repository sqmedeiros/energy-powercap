# ﷽
from itertools import accumulate, combinations
import math
import sys
input = lambda: sys.stdin.readline().strip()
def solve():
    n,m=[int(i) for i in input().split()]
    l=[int(i) for i in input().split()]
    tot=0
    s=1
    for i in range(1,m+1): 
        for j in combinations(l,i):
            t1=1
            for k in j:t1*=k


            if s==1:tot+=n//t1 
            else:tot-=n//t1 

        s*=-1
    print(tot)



if __name__ == "__main__":
    # for i in range(int(input())):
        solve()