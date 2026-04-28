n = int(input())
arr = list(map(int,input().split()))
curr,res =  arr[0],arr[0]
for c in arr[1:]:
    curr = max(c,curr+c)
    res = max(res,curr)
print(res)