def minimum_coins(coins: list, target: int) -> int:
    visited = set()
    visited.add(target)
    queue = [(target, 0)]
    while len(queue) > 0:
        current = queue.pop(0)
        current_target = current[0]
        current_count = current[1]
        for coin in coins:
            new_target = current_target - coin
            if new_target == 0:
                return current_count + 1
            if new_target > 0 and not(new_target in visited):
                queue.append((new_target, current_count + 1))
                visited.add(new_target)

    return -1


def minimum_coins2(coins: list, target: int) -> int:
    table = [-1 for i in range(target + 1)]
    table[0] = 0
    for i in range(target):
        if table[i] != -1:
            for coin in coins:
                coin_sum = i + coin
                if coin_sum <= target:
                    total_coins = table[i] + 1
                    if total_coins < table[coin_sum] or table[coin_sum] == -1:
                        table[coin_sum] = total_coins

    return table[target]


n, x = input().split(" ")
x = int(x)
c = input().split(" ")
c = [int(ci) for ci in c]
print(minimum_coins2(c, x))