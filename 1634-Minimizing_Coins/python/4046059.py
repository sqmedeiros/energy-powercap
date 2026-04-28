import sys
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    import io,os
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# def dfs(node):
#     print(node)
#     visited[node] = True                           #1 indexing 

#     for i in adj[node]:
#         if not visited[i]:
#             visited[i] = True
#             dfs(i)




N,X=[int(i) for i in input().split()]
C =[int(i) for i in input().split()]

C.sort()

dp = [10**7]*(X+1)
dp[0] = 0
for i in range(1,X+1):
    for j in range(N):
        if i-C[j]>=0:
            dp[i]=min(dp[i],dp[i-C[j]]+1)
        else:
            break 
if dp[X]==10000000:
    sys.stdout.write("-1\n")
else:
    sys.stdout.write(str(dp[X]) +"\n")

    # if len(relevant_C)==1:
    #     print(0)
    # else:
    #     n = len(relevant_V)
    #     idx = len(relevant_V)-1
    #     mex = relevant_V[-1]
    #     nlo = [-1]*n


    #     for i in range(2,1+n):
    #         if relevant_V[-i] > mex:
    #             mex = relevant_V[-i]
    #             nlo[-i] = idx
    #             idx = n-i 
    #         else:
    #             nlo[-i] = idx
    #     i = 0
    #     score = 0
    #     Alice = False
    #     while i<n:
    #         if not Alice:
    #             score -= relevant_V[i]
    #             if nlo[i]==-1:
    #                 break
    #             i = nlo[i]

    #         else:
    #             score += relevant_V[i]
    #             if nlo[i]==-1:
    #                 break
    #             i = nlo[i]
    #         Alice = not Alice
    #     print(score)
# for i in range(1,101):
#     print(i, '{:017b}'.format(i))