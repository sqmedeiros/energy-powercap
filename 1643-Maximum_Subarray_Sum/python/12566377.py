n = int(input())
x = list(map(int, input().split()))

maxSum = x[0]
currSum = x[0]
for i in range(1, n):
    currSum = max(x[i], currSum + x[i])
    maxSum = max(maxSum, currSum)
print(maxSum)