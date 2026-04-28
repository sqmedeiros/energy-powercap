x=int(input())
data=list(map(int,input().split()))
max_sum=float('-inf')
current_sum=0
for y in data:
    current_sum+=y
    max_sum=max(max_sum,current_sum)
    current_sum=max(current_sum,0)
print(max_sum)