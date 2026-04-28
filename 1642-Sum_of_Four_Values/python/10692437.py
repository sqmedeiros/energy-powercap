n,x=map(int,input().split())
a=list(map(int,input().split()))
sum_pair={}
for i in range(n):
    for j in range(i+1,n,1):
        sum_pair[a[i]+a[j]]=[i,j]
def sol():
    global n
    global x
    global a
    global sum_pair
    for i in range(n):
        for j in range(i+1,n,1):
            k=x-a[i]-a[j]
            if k in sum_pair and j<sum_pair[k][0]:
                print(i+1,j+1,sum_pair[k][0]+1,sum_pair[k][1]+1)
                return
    print('IMPOSSIBLE')
sol()

