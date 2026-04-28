def printRes(res):
    for i in res:
        if type(i) == tuple:
            print(*i, sep = '\n')
        elif type(i) == list:
            print(*i)
        else:
            print(i)

def minp(func = int):
    return map(func, input().split())

def sinp(func = int):
    return func(input())

def linp(func = int):
    return list(minp(func))

def start():
    res = []
    # for _ in range(int(input()) - 1): res.append(main())
    res.append(main())
    printRes(res)

def main():
    n, x = minp()
    a = linp()
    a = sorted([[i, a[i]] for i in range(n)], key = lambda x: x[1])
    for i in a:
        target = x - i[1]
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid][1] == target and a[mid][0] != i[0]:
                return [i[0] + 1, a[mid][0] + 1]
            elif a[mid][1] < target:
                left = mid + 1
            else:
                right = mid - 1
    return "IMPOSSIBLE"


start()