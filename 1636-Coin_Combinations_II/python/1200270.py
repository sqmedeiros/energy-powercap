from sys import stdin, stdout
#stdin = open('Coin Combinations 2.txt', 'r')
def MI(): return map(int, stdin.readline().split())
def LI(): return list(map(int, stdin.readline().split()))

mod=10**9+7
n,x=MI()
c=LI()
c=[v for v in c if v<=x]
dp=[1]+[0 for i in range(x)]

for v in c:
    for i in range(v,x+1):
        dp[i]=(dp[i]+dp[i-v])%mod
stdout.write("{}\n".format(dp[x]))