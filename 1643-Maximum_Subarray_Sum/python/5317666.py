length = int(input())
arr = [int(x) for x in input().split()]

currentSum = 0
maxSum = 0
maxVal = arr[0]
allNegative = True
for i in range(0, length):
    if(arr[i] >= 0):
        allNegative = False
    maxVal = max(maxVal,arr[i])
    currentSum = currentSum + arr[i]
    if currentSum < 0:
        currentSum = 0
    maxSum = max(maxSum, currentSum)
if(allNegative):
    print(maxVal)
else:
    print(maxSum)