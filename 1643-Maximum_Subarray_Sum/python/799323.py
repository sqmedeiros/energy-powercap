


t=int(input())

n=list(map(int,input().split()))

currentMax=globalMax=n[0]

for i in range(1,t):
    currentMax=max(n[i],currentMax+n[i])
    if currentMax>globalMax:
        globalMax=currentMax
print(globalMax)