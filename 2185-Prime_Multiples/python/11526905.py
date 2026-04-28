l1 = input().split(" ")
n = int(l1[0])
k = int(l1[1])

l2 = input().split(" ")
l = []

for i in l2:
    l.append(int(i))

def count_bits(n):
    cnt = 0
    while n > 0:
        cnt += n % 2
        n //= 2
    return cnt

ans = 0
for mask in range(1, 1 << k):
    n1 = 1
    for i in range(0, k):
        flag = mask & (1 << i)
        if flag:
            n1 *= l[i]

    if n1 <= n:
        cnt = count_bits(mask)
        if cnt & 1:
            ans += n // n1
        else:
            ans -= n // n1

print(int(ans))