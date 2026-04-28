n,joincnt=map(int,input().split())
adjcent=[[] for _ in range(n+1)]
team=[0]*(n+1)
stack=[]
check=True
for _ in range(joincnt):
    a,b=map(int,input().split())
    adjcent[a].append(b)
    adjcent[b].append(a)
for i in range(1,n+1):
    if team[i]!=0:
        continue
    stack.append(i)
    team[i]=1
    while stack and check:
        node=stack.pop()
        for element in adjcent[node]:
            if team[element]!=0:
                if team[element]==team[node]:
                    check=False
                    break
            else:
                team[element]=1+(team[node]==1)
                stack.append(element)

if check:
    team.remove(0)
    print(*team)
else:
    print('IMPOSSIBLE')
