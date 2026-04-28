n, k = map(int,input().split())
v = list(map(int,input().split()))

def ans(i, p, mul):
    if i == k:
        if p == 0:
            return 0
        elif p%2 == 1:
            return (n//mul)
        else:
            return -(n//mul)

    return ans(i+1,p+1,mul*v[i]) + ans(i+1,p,mul)

print(ans(0,0,1))