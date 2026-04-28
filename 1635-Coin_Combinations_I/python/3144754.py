# The first input line has two integers n
#  and x
# : the number of coins and the desired sum of money.

# The second line has n
#  distinct integers c1,c2,…,cn
# : the value of each coin.
# from sys import stdin

n,x=map(int,input().split())
c=list(map(int,input().split()))
# c.sort()
MOD=10**9+7
dp_solve=[0]*(x+1)
dp_solve[0]=1
for i in range(1, x+1):
    for coin in c:
        # val=c[j]
        # diff=i-val
        # if diff >= 0:
        if coin <= i:
            # print(x-val)
            dp_solve[i] += (dp_solve[i-coin] % MOD) 
            # dp_solve[i] %= MOD
        # else:
        #     break

print(dp_solve[x] % MOD)