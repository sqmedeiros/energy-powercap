## Building Teams 
from collections import deque

n , m = map(int , input().split()) 

aj = [[] for _ in range(n+1)] 

for i in range(m):

    a , b = map(int , input().split()) 

    aj[a].append(b) 

    aj[b].append(a) 

visited = [False]*(n+1) 

components = []

def bfs(st:int):

    queue = deque([st]) 

    while queue :

        visited[i] = True 

        curr = queue.popleft() 

        for neighbor in aj[curr]:

            if not visited[neighbor]:

                visited[neighbor] = True

                queue.append(neighbor)


for i in range(1 , n+1):

    if not visited[i]:

        components.append(i)

        bfs(i) 


k = len(components)-1 

print(k)

for i in range(k):

    print(components[i] , components[i+1])


