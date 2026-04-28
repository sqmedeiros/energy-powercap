import sys
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int, input().split()))
outs = []
sys.setrecursionlimit(2*10**6)
MOD = 10**9+7

for __ in range(1):
    n,x= inp()
    c = inp()
    dp = [0]*(x+1)
    for now_at in range(x,-1,-1):
        if dp[now_at]==0 and now_at!=x:continue
        for to_take in c:
            if now_at>=to_take:
                if dp[now_at-to_take]:
                    dp[now_at-to_take]= min(dp[now_at-to_take],dp[now_at]+1)
                else:
                    dp[now_at-to_take]=dp[now_at]+1
    outs.append(dp[0] if dp[0] else -1)

print("\n".join(map(str, outs)))