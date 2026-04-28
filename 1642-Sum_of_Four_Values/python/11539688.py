def main():
    import sys
    n,m,*a=map(int, sys.stdin.read().strip().split())

    a = [(ai, i+1) for i, ai in enumerate(a)]
    a = sorted(a)


    d = 0
    while d<n:
        i = d+1
        while i < n:
            j = i+1
            k = n-1
            target = m-a[i][0]-a[d][0]
            while j<k:
                complement = a[k][0] + a[j][0]

                if complement < target:
                    j += 1
                elif complement > target:
                    k -= 1
                else:
                    print(a[d][1], a[i][1], a[j][1], a[k][1])
                    return


            cur = a[i][0]
            while i<n and cur==a[i][0]:
                i += 1

        cur = a[d][0]
        while d < n and cur == a[d][0]:
            d += 1

    print("IMPOSSIBLE")

main()
