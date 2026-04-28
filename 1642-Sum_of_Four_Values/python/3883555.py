n, x = map(int, input().split())
nums = list(map(int, input().split()))
pairs = {}
pair = 0
ans = 0
for i in range(n):
    if ans > 0:
        break
    for j in range(i+1, n):
        pair = nums[i] + nums[j]
        diff = x - pair 
        if diff in pairs:
            a,b = pairs[diff]
            print(i+1,j+1,a+1,b+1)
            ans = 1
            break
    for k in range(0,i):
        pair = nums[i] + nums[k]
        if pair not in pairs:
            pairs[pair] = [i, k]
if ans==0:
    print('IMPOSSIBLE')