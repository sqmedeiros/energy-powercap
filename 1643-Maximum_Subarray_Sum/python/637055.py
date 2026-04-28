import sys
# sys.stdin = open("input.txt", "r")

w = int(input())
arr = list(map(int, input().split()))

dp = [float("-inf")]*len(arr)

for i, ele in enumerate(arr):
    dp[i] = max(dp[i-1]+ele, ele)
print(max(dp))