n, x = map(int, input().split())

c = list(map(int, input().split()))


num_ways = [0]*(x+1)
num_ways[0] = 1

for i in range(1, len(num_ways)):
    for coin in c:
        if i - coin >= 0:
            num_ways[i] += num_ways[i-coin]

    num_ways[i] %= (10**9 + 7)


print(num_ways[x])