from collections import defaultdict,deque
n,m = map(int,input().split())
graph = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

group1 = set()
group2 = set() 
nums = ['-1'] * n
q = deque()
valid = True
for i in range(1,n+1):
    if i not in group1 and i not in group2:
        q.append((i,1))
        group1.add(i)
        nums[i-1] = '1'
        while q:
            node,group = q.popleft()
            for neb in graph[node]:
                if group == 1:
                    if neb in group1:
                        valid = False
                        break
                    elif neb not in group2:
                        group2.add(neb)
                        nums[neb-1]  = '2'
                        q.append((neb,2))
                else:
                    if neb in group2:
                        valid = False
                        break
                    elif neb not in group1:
                        group1.add(neb)
                        q.append((neb,1))
                        nums[neb-1]  = '1'

print(' '.join(nums) if valid else 'IMPOSSIBLE')