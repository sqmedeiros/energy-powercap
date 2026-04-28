n = int(input())
arr = list(map(int,input().split()))
ans, curr_sum = arr[0], arr[0]
for i in range(1,n):
    curr_sum = max(arr[i],arr[i]+curr_sum)
    ans = max(ans,curr_sum)
print(ans)

# i/p ==>
# 8
# -1 3 -2 5 3 -5 2 2
# o/p ==>
# 9