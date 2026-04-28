from collections import Counter
N, X = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)
for z in range(N):
    for i in range(z+1, N):
        k = N-1
        for j in range(i+1, N-1):
            t = X-B[i]-B[j]-B[z]
            while k > j and B[k] > t:
                k -= 1
            if k > j and B[k] == t:
                s = Counter([B[i], B[j], B[k], B[z]])
                for i, v in enumerate(A):
                    if s[v]:
                        print(i+1, end=" ")
                        s[v] -= 1
                print()
                exit()
            elif k <= j:
                break
print("IMPOSSIBLE")