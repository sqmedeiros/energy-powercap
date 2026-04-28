# bfs / space-complex DP

# from collections import deque

# N, X = map(int, input().split(" "))
# coinVals = list(map(int, input().split(" ")))

# queue = deque()

# queue.append([0, 0])

# xCount = 0

# while len(queue) > 0:
#     elem = queue.popleft()
#     for val in coinVals:
#         if elem[1] <= val:
#             if elem[0] + val < X:
#                 queue.append([elem[0] + val, val])
#             elif elem[0] + val == X:
#                 xCount += 1

# print(xCount)




# optimized DP

MOD = 10**9 + 7

N, X = map(int, input().split(" "))
coinVals = list(map(int, input().split(" ")))

dp = [0] * (X+1)
dp[0] = 1

for x in coinVals:
    for i in range(X+1):
        if i-x >= 0:
            dp[i] = (dp[i] + dp[i-x]) % MOD

print(dp[X])