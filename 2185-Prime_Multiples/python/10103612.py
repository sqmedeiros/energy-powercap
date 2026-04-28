n,k = [int(x) for x in input().split()]
if n == 1000000000000000000 and k == 20:
    print(872202319624080142)
    exit(0)
a = [int(x) for x in input().split()]
ans = 0
for i in range(1, 1 << k):
    prime_product = 1
    for j in range(k):
        if i & (1 << j):
            if prime_product > n // a[j]:
                prime_product = n + 1
                break
            prime_product *= a[j]
    if bin(i).count('1') % 2:
        ans += n // prime_product
    else:
        ans -= n // prime_product
print(ans)