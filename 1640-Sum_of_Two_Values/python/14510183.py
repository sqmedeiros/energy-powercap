from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

n,x=map(int,input().split())
a=list(map(int,input().split()))
a=[Wrapper(i) for i in a]
dih={}
flag=1
for i in range(n):
    if Wrapper(x-a[i]) in dih:
        print(dih[Wrapper(x-a[i])]+1,i+1)
        flag=0
        break
    dih[a[i]]=i
if flag:
    print("IMPOSSIBLE")