def four_sum_positions(n, x, a):
    from collections import defaultdict

    seen = dict()  # sum -> (i, j)

    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            need = x - curr

            if need in seen:
                p, q = seen[need]
                # ensure all indices are distinct
                if p != i and p != j and q != i and q != j:
                    print(p + 1, q + 1, i + 1, j + 1)
                    return

        # add pairs ending at i *after* checking
        for j in range(i):
            seen[a[j] + a[i]] = (j, i)

    print("IMPOSSIBLE")

n, x = map(int, input().split())
a = list(map(int, input().split()))
four_sum_positions(n,x,a)