def specialHashTwoPointer(values: list, n: int, x: int) -> str:
    somas = {}

    for i in range(n-1):
        for j in range(i + 1, n):
            somas[values[i][0] + values[j][0]] = (i, j)

    for i in range(n-1):
        for j in range(i + 1, n):
            sum = values[i][0] + values[j][0]

            if x - sum in somas:
                p = somas[x-sum]

                if p[0] != i and p[0] != j and p[1] != i and p[1] != j:
                    return f"{values[i][1] + 1} {values[j][1] + 1} {values[p[0]][1] + 1} {values[p[1]][1] + 1}"

    return "IMPOSSIBLE"

n, x = map(int, input().split())
valuesOriginal = list(map(int, input().split()))

values = [[valuesOriginal[i], i] for i in range(n)]

print(specialHashTwoPointer(values, n, x))