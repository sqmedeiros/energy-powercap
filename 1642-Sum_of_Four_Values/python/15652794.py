n , x = map(int,input().split())
nums = list(map(int,input().split()))
di = {}
for i in range(n):
    for j in range(i+1,n):
        k = nums[i] + nums[j]
        if k not in di :
            di[k] = [(i+1,j+1)]
        else :
            di[k].append((i+1,j+1))
found = False
for i in di :
    l = x - i 
    if l == i :
        if len(di[i]) >= 2:
            for k in di[i]:
                for j in di[i]:
                    if i != j and len(set(k+j)) == 4 :
                        print(*(k+j))
                        found = True
                        break 
                if found :
                    break 
    if found :
        break
    else :
        if l in di :
            for k in di[i] :
                for m in di[l]:
                    if len(set(k+m)) == 4 :
                        print(*(k+m))
                        found = True
                        break 
                if found :
                    break 
    if found :
        break
else :
    print("IMPOSSIBLE")
