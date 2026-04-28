import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

MOD = int(1e9 + 7)

c_cnt, sum = (int(token) for token in input().split())
c = [int(ci) for ci in input().split()]

dp = [0] * (sum+1)
dp[0] = 1

#for ci in c:
    #for s in range(sum):
        #if (s + ci > sum):
            #break
     #   if (s + ci <= sum):
      #      dp[s + ci] += dp[s]
       #     dp[s + ci] %= MOD

for s in range(0, sum):
    cur_v = dp[s]
    if (cur_v == 0):
        continue;
    for cj in c:
        if (s + cj <= sum):
            dp[s + cj] = (dp[s + cj] + cur_v) % MOD 

print(dp[sum])