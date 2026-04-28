n,m = map(int,input().split())
path = {}
for i in range(1,n+1):
    path[i] = []
for i in range(m):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
need_to_built = []
check = set()
for i in path :
    if path[i] == -1 :
        continue
    elif path[i] == []:
        need_to_built.append(i)
    else :
        if i not in check :
            check.add(i)
            list_1 = path[i]
            path[i] = -1
            while list_1 :
                m = list_1.pop()
                if m not in check :
                    check.add(m)
                    list_1 += path[m]
                    path[m] = -1
        need_to_built.append(check.pop())
        check = set()
x = len(need_to_built)
print(x - 1)
for i in range(1,x):
    print(need_to_built[0],need_to_built[i])