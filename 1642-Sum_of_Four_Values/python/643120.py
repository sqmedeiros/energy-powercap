def findFourElements (arr, n, X):
    mp = {} 
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j] 
    for i in range(n - 1):
        for j in range(i + 1, n):
            summ = arr[i] + arr[j]
            if (X - summ) in mp:
                p = mp[X - summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                    print(i+1,j+1,p[0]+1,p[1]+1)
                    return
    print("IMPOSSIBLE")
    return
n,X=map(int,input().split())
arr=[int(x) for x in input().split()]
findFourElements(arr, n, X) 