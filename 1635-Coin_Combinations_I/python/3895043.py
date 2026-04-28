n,x = map(int, input().split())
arr = [*map(int,input().split())]
lis = [0 for i in range(x+1)]
lis[0] = 1
for i in range(1,x+1):
    for item in arr:
        if i <item:
            continue
        lis[i] += lis[i-item]
        lis[i]%= (10**9 + 7)
# print(*lis)        
print(lis[x])



# ans = 0
# def helper(rem):
#     global ans
#     if rem == 0:
#         ans += 1
#     if rem<0:
#         return
#     for item in arr:
#         helper(rem -item)
# helper(x)
# print(ans)