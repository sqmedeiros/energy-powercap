def solve(a,n,x):
    ts = {}
    for i in range(n):
        for j in range(i+1, n):
            s = a[i]+a[j]
            s = f"{s}"
            if s in ts:
                ts[s].append((i,j))
            else:
                ts[s] = [(i,j)]
    for sm in ts:
        if f"{x-int(sm)}" in ts:
            pr = pairs(ts[sm], ts[f"{x-int(sm)}"])
            if pr:
                print(pr[0][0]+1, pr[0][1]+1, pr[1][0]+1, pr[1][1]+1)
                return
    print("IMPOSSIBLE")
    return


def pairs(l1, l2):
    # return two unequal pairs in l1 and l2
    for p1 in l1:
        for p2 in l2:
            if p1[0] != p2[0] and p1[0] != p2[1] and p1[1] != p2[0] and p1[1] != p2[1]:
                return p1, p2
    return None

n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
solve(a, n, x)