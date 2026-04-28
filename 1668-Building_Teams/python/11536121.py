n,m = list(map(int,input().split()))
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    friends[a].append(b)
    friends[b].append(a)

team = [0 for i in range(n+1)]
team[1] = 1
stack = []
invalid = False
def dfs(x):
    global invalid
    stack = [x]
    while(len(stack)):
        s = stack[-1]
        stack.pop()
        for y in friends[s]:
            if(team[y]==0):
                stack.append(y)
                if(team[s]==1):
                    team[y] = 2
                else:
                    team[y] = 1
            else:
                if(team[y]==team[s]):
                    invalid = True

dfs(1)
for x in range(2,n+1):
    if(not team[x]):
        team[x] = 1
        dfs(x)
if(invalid):
    print("IMPOSSIBLE")
else:
    for i in range(1,len(team)):
        print(team[i],end = " ")
    print()

