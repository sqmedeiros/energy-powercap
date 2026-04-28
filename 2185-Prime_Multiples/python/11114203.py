def REK(partial_product, index, pop):
    global n,k
    if partial_product > n:
        return 0

    if index >= k:
        if partial_product == 1:
            return 0
        ans = (n//partial_product) * (-1)**(1 + (pop%2))
        return ans

    ans = REK(partial_product, index+1, pop)
    ans += REK(partial_product*p[index], index+1, pop+1)
    return ans

n, k = map(int, input().split())
p = list(map(int, input().split()))

print(REK(1,0,0))