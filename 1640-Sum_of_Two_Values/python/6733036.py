n,x = list(map(int, input().split()))

arr = list(map(int, input().split()))

d = [(arr[i],i) for i in range(len(arr))]
d.sort()

i,j = 0, len(arr)-1
flag = True
while i<j:
    if d[i][0]+d[j][0]==x:
        print(d[i][1]+1, d[j][1]+1)
        flag = False
        break
    elif d[i][0] + d[j][0] > x:
        j-=1
    else:
        i+=1

if flag:
    print("IMPOSSIBLE")