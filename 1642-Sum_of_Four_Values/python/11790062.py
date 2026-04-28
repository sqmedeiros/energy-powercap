import time


def process(n, x, a):
    if len(a) < 4:
        return -1
    pom0 = []
    a = [(a[i], i) for i in range(n)]
    a.sort()
    if sum([x[0] for x in a[:4]]) > x:
        return -1
    if sum([x[0] for x in a[-4:]]) < x:
        return -1
    for i in range(n):
        for j in range(i + 1, n):
            c = a[i][0] + a[j][0]
            if c > x - 2:
                break
            pom0.append((c, a[i][1], a[j][1]))
    if len(pom0) < 2:
        return -1
    pom0.sort(key=lambda x: x[0])
    # pom = []
    # for i in range(len(pom0)):
    #     if i >= 2 and pom0[i][0] == pom0[i - 1][0] and pom0[i][0] == pom0[i - 2][0]:
    #         continue
    #     pom.append(pom0[i])
    # pom0 = pom
    #print(len(pom0))
    #print(pom0)
    i, j = 0, len(pom0) - 1
    if pom0[-1][0] + pom0[-2][0] < x:
        return -1
    if pom0[0][0] + pom0[1][0] > x:
        return -1
    it = 0
    while i < j:
        it += 1
        d = pom0[i][0] + pom0[j][0]
        if d == x:
            s = set([pom0[i][1], pom0[i][2], pom0[j][1], pom0[j][2]])
            if len(s) == 4:
                #print(it)
                print(pom0[i][1] + 1, pom0[i][2] + 1, pom0[j][1] + 1, pom0[j][2] + 1)
                return 0
            else:
                d0 = pom0[i+1][0] - pom0[i][0]
                d1 = pom0[j][0] - pom0[j-1][0]
                if d0 < d1:
                    i += 1
                else:
                    j -= 1
        elif d < x:
            i += 1
        else:
            j -= 1
    #print(it)
    return -1

n, x = map(int, input().split())
a = list(map(int, input().split()))
start_time = time.time()
if process(n, x, a) == -1:
    print("IMPOSSIBLE")

#print("--- %s seconds ---" % (time.time() - start_time))