n,k = map(int,input().split())
primes = list(map(int,input().split()))

#print ("primes",primes)

def popcount(v):
    ret= 0
    while v:
        v=v&(v-1)
        ret+=1
    return ret

tot=0
for i in range(1,(1<<k)):
    prod=1
    for j in range(k):
        if (i&(1<<j))!=0:
            inverse_cur_sz= primes[j];  
            prod*=inverse_cur_sz
            if (prod>n):break
    factor=-1
    if (popcount(i)%2==1):
        factor=1

    v = n // prod
    #print (v)
    tot += factor* v

print(tot)