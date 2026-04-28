n, m = list(map(int, input().split()))
g = {}
a = list(map(int, input().split()))
for i in range(n):
  for j in range(i+1, n):
    s = a[i] + a[j] ; 
    if s not in g :
      g[s] = []
    g[s].append({ i+1,j+1 })

for i in g:
  j = m - i ;
  for x in g[i] :
    for y in g.get(j, []):
      if not x & y:
        print (*x|y) 
        exit()

print ("IMPOSSIBLE")