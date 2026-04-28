n,x = list(map(int, input().split())) 
arr = list(map(int , input().split())) 

seen = {}
for i in range(n):
    for j in range(i + 1, n):
        comp = x - (arr[i] + arr[j]) 
        if comp in seen:
            print(i + 1,j + 1,seen[comp][0] + 1, seen[comp][1] + 1)
            exit()
    for j in range(i):
        seen[arr[i] + arr[j]] = [i,j] 

print("IMPOSSIBLE") 