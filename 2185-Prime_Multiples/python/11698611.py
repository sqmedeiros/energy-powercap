I = lambda : map(int,input().split())

n,k = I()
primes = list(I())

def crible():
    global n, k, primes
    ans = 0

    for mask in range(1<<k):
        product,size = 1,0
        for i in range(k):
            if (1<<i)&mask :
                product *= primes[i]
                size += 1
                if product > n :
                    break
        if size%2 == 0:
            ans -= (n//product)
        else :
            ans += (n//product)
    ans += n
    return ans

ans = crible()
print(ans)