MOD = 10**9 + 7
arr = input().split()
num_coins = int(arr[0])
x = int(arr[1])
coins = [int(i) for i in input().split()]

array = [0 for i in range(x+1)]
array[0] = 1
for coin in coins:
    for j in range(1, x + 1):
        if (j - coin >= 0):
            array[j] += array[j - coin]
            array[j] %= MOD
print(array[x])

# array = [[0 for i in range(x + 1)] for j in range(num_coins + 1)]
# array[0][0] = 1
# for i in range(1, num_coins + 1):
#     coin = coins[i-1]
#     for j in range(x + 1):
#         if (coin >= 1):
#             array[i][j] += (array[i-1][j] % MOD)
#         if (j - coin >= 0):
#             array[i][j] += (array[i][j - coin] % MOD)
# print(array[num_coins][x])