from random import getrandbits

RANDOM = getrandbits(32)

class RandDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key ^ RANDOM, value)
    def __getitem__(self, key):
        return super().__getitem__(key ^ RANDOM)
    def __contains__(self, key):
        return super().__contains__(key ^ RANDOM)


n,x=map(int,input().split())
a=list(map(int,input().split()))
dih=RandDict()
flag=1
for i in range(n):
    if x-a[i] in dih:
        print(dih[x-a[i]]+1,i+1)
        flag=0
        break
    dih[a[i]]=i
if flag:
    print("IMPOSSIBLE")