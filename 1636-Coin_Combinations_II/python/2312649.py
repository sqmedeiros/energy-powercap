n,s=input().split()
n,s=int(n),int(s)
a=list(map(int,input().rstrip().split()))
b=[0 for _ in range(s+1)]
b[0]=1
MOD=1000000007
for x in a:
    # b[x]+=1
    for y in (range(x,s+1)):
        b[y]+=b[y-x]%MOD 
        b[y]%=MOD
# print(b)
print(b[s])
