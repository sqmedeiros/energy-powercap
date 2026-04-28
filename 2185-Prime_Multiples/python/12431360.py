n,k=input().split()
L=[int(x) for x in input().split()]
n=int(n)
k=int(k)
som=0
for i in range(1,pow(2,k)):
    somme=0
    summer=1
    more=i
    turn=0
    while(more>0):
        somme+=more%2
        if(more%2==1):
            summer*=L[turn]
        more=more//2
        turn+=1
    if(somme%2==1):
        som+=n//summer
    else:
        som-=n//summer
print(som)