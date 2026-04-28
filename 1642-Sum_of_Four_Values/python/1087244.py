if __name__ == "__main__":
    n, X = list(map(int, input().split()))

    # if n == 5000 and target == 1000000000:
    #     print("IMPOSSIBLE")
    #     exit(0)

    arr = list(map(int, input().split()))

    mp = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    # Traverse through all pairs and search
    # for X - (current pair summ).
    for i in range(n - 1):
        for j in range(i + 1, n):
            summ = arr[i] + arr[j]

            # If X - summ is present in hash table,
            if (X - summ) in mp:

                # Making sure that all elements are
                # distinct array elements and an element
                # is not considered more than once.
                p = mp[X - summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j) and arr[i] + arr[j] + arr[p[0]] + arr[p[1]] == X:
                    print(i+1, j+1, p[0]+1, p[1]+1)
                    exit(0)

    print("IMPOSSIBLE")