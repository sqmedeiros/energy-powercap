#Input:

#4 8
#2 7 5 1

a, b = map(int, input().split())
c = list(map(int, input().split()))
if b == 1:
    print("IMPOSSIBLE")
    exit()
m = {}
for i, n in enumerate(c):
    part = b - n  
    if part in m:

        print(m[part] + 1, i + 1) 

        exit()
    else:
        m[n] = i  

print("IMPOSSIBLE")