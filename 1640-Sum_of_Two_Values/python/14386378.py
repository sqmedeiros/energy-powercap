def main():
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))

    tuplas = list(enumerate(nums))        # [(0,30), (1,10), (2,20)]

# ordenamos por el valor
    tuplas.sort(key=lambda x: x[1])      # [(1,10), (2,20), (0,30)]

    a = 0
    b = len(tuplas) - 1
    sum = 0

    while a < b:
        sum += tuplas[a][1] + tuplas[b][1]
        if sum == x:
            print(tuplas[a][0] + 1, tuplas[b][0] + 1)
            return

        if sum > x:
            b -= 1
        else:
            a += 1

        sum = 0

    print("IMPOSSIBLE")
    return

main()