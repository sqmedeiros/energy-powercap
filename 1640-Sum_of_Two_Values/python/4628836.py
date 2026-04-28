n, value = map(int,input().split())
arr = list(map(int, input().split()))

if(n>1):
    arr1 = list()
    for i,y in enumerate(arr):
        arr1.append((y,i+1))

    arr1.sort()
    j=n - 1
    i=0
    while(i<j):
        if(arr1[i][0]+arr1[j][0] == value):
            print(arr1[i][1], arr1[j][1])
            break

        elif(arr1[i][0]+arr1[j][0] < value):
            i+=1
            continue

        elif(arr1[i][0]+arr1[j][0] > value):
            j-=1
            continue

    if(i==j):
        print("IMPOSSIBLE")

else:
    print("IMPOSSIBLE")