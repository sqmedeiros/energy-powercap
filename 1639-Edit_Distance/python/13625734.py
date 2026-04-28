A,B = open(0)
*R,_ = *l, = range(len(A))
for c in B:
    k = l[:]
    l[0] += 1
    for j in R:
        l[j + 1] = 1 + min(l[j], k[j + 1], k[j] - (A[j] == c))
print(k[-1])