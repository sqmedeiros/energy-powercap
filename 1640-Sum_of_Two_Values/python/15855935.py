n, x = map(int, input().split())
a = list(map(int, input().split()))
aa = sorted(a)
r = n-1
s = aa[0] + aa[n-1]
found = False
for l in range(n-1):
    while l < r-1 and s > x:
        s = s - aa[r] + aa[r-1]
        r -= 1
    if s == x:
        if aa[l] == aa[r]:
            print(a.index(aa[l]) + 1, a.index(aa[r], a.index(aa[l])+1) + 1)
        else:
            print(a.index(aa[l]) + 1, a.index(aa[r]) + 1)
        found = True
        break
    s = s - aa[l] + aa[l+1]
if found == False:
    print("IMPOSSIBLE")