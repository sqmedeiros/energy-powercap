n = int(input())
nums = list(map(int,input().split()))

mSum = 0 
s = 0 
maxi = float('-inf')

for i in range(n):
    s += nums[i]

    maxi = max(maxi , nums[i])

    if s < 0:
        s = 0 

    mSum = max(mSum , s)

if mSum == 0 and maxi < 0:
    print(maxi)
else:
    print(mSum)