n=int(input())
num=list(map(int,input().split()))
sum=0
maxsum=-10**9
for val in num:
    sum+=val
    maxsum=max(maxsum,sum)
    if sum<0:
        sum=0
print(maxsum)