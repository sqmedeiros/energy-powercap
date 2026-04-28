n,x=map(int,input().split())
arr=list(map(int,input().split()))
mp={}

for i in range(n):
    for j in range(i+1,n):
        missing=x-arr[i]-arr[j]

        if missing in mp:
            print(i+1,j+1,*mp[missing])
            exit()

    for j in range(i):
        mp[arr[j]+arr[i]]=[i+1,j+1]

print('IMPOSSIBLE')       