import sys

n, sum = map(int,input().split())
denom = list(map(int, input().split()))

dp=[10**10]*1000005
dp[0]=0

#push dp is different cuz u want to propagate already

for i in range(n): #for every coin
    for w in range(denom[i],sum+1): #for every sum below coin
        # print(i,w)
        dp[w] = min(dp[w],dp[w-denom[i]]+1)

# def coin(rem, depth):
#     # mini=10**10
#     # if (rem,depth) in memo: return memo[(rem,depth)]
#     # if rem==0: 
#     #     memo[(rem,depth)]=depth
#     #     return depth
#     # elif rem<0: 
#     #     memo[(rem,depth)]=10**10
#     #     return 10**10
#     # for d in denom:
#     #     mini=min(coin(rem-d,depth+1),mini)

#     return mini

print(-1 if dp[sum]==10**10 else dp[sum])
# print(-1 if coin(sum,0)==10**10 else coin(sum,0))

