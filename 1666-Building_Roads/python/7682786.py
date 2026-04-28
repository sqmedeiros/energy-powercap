n,m=map(int,input().split())
par=[el for el in range(n)]

def find(x):
    st=[]
    while x!=par[x]:
        st.append(x)
        x=par[x]
    for el in st:
        par[el]=x
    return x

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    par[find(a)]=find(b)

for el in range(n):
    find(el)
seen=set()
for el in par:
    seen.add(el)
seen=[el for el in seen]
print(len(seen)-1)
i=1
for _ in range(len(seen)-1):
    print(seen[0]+1,seen[i]+1)
    i+=1