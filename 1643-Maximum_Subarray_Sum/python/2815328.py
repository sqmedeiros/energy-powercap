
# n, target = map(int, input().split())
n = int(input())
arr = list(input().split())
temp = [int(i) for i in arr]
# for i in range(n):
#     res = []
#     a = list(input().split())
#     for j in a:
#         res.append(int(j))
#     temp.append(res)

#temp.sort(key = lambda x: x[0])

#code starts here
maxi = float('-inf')
local_max = 0

for i in temp:
    local_max += i
    if maxi < local_max:
        maxi = local_max
    if local_max < 0:
        local_max = 0
print(maxi)
