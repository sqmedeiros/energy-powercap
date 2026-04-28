n, _sum = list(map(int, input().split()))
A = list(map(int, input().split()))
A = sorted(zip(A, range(1, len(A)+1)), key=lambda x: x[0])

s, e = 0, len(A)-1
while s < e:
    tot = A[s][0] + A[e][0]
    if tot == _sum:
        print(A[s][1], A[e][1])
        break
    if tot > _sum: e -= 1
    else: s += 1
else: print("IMPOSSIBLE")