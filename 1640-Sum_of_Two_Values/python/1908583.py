x=int(input().split(" ")[1])
i=1
d={}
for e in input().split(" "):
 e=int(e)
 if e in d:print(d[e],i)
 d[x-e]=i
 i+=1
print("IMPOSSIBLE")