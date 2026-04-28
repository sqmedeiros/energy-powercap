coin_num, des_sum = map(int, input().split(" "))
coins = [int(x) for x in input().split(" ")]
INFINITY = des_sum + 1
memory = [INFINITY] * (max(des_sum, max(coins)) + 1)

for coin in coins:
    memory[coin] = 1

for coin in coins:
    for i in range(coin, des_sum + 1):
        if i - coin >= 0 and memory[i - coin] + 1 < memory[i]:
            memory[i] = memory[i - coin] + 1

if memory[des_sum] == INFINITY:
    print(-1)
else:
    print(memory[des_sum])