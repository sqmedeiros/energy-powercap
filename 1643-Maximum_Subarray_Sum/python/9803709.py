n=int(input())
arr=list(map(int, input().split()))
s,max_so_far=0,float('-inf')
for num in arr:
    s=max(num,s+num)
    max_so_far=max(max_so_far,s)
    if s < 0:
        s=0
print(max_so_far)