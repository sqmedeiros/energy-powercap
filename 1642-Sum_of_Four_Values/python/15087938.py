from collections import defaultdict


n,sum = map(int,input().split())

v = list(map(int,input().split()))

m = defaultdict(list)

for i in range(n-1):
    for j in range(i+1,n):
        sumi = v[i]+v[j]
        m[sumi].append((i,j))


for i in range(n-3):
    for j in range(i+1,n-2):
        req = sum - v[i]-v[j]

        for pair in m[req]:
            a = pair[0]
            b = pair[1]

            if a!=i and a!=j and b!=i and b!=j:
                print(f"{i+1} {j+1} {a+1} {b+1}")
                exit()

print("IMPOSSIBLE")