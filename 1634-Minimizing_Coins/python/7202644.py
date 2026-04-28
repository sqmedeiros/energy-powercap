import sys
n, x = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
v.sort()
#print(v)
dp = [0]

for i in range(1, x+1):
    dp.append(sys.maxsize)
    #dp[i] = sys.maxsize
    for val in v:
        if val > i:
            break
        else: #val <= i
            if dp[i-val] != -1:
                if dp[i-val] + 1 < dp[i]:
                    dp[i] = dp[i-val] + 1
    if dp[i] == sys.maxsize:
        dp[i] = -1
print(dp[x])


