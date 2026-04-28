import sys
input = sys.stdin.readline
from collections import deque

def coin_change(coins, amount):
    visited = [False] * (amount + 1)
    queue = deque([(0, 0)])  # (current_amount, steps)

    while queue:
        curr, steps = queue.popleft()
        if curr == amount:
            return steps
        for coin in coins:
            next_amt = curr + coin
            if next_amt <= amount and not visited[next_amt]:
                visited[next_amt] = True
                queue.append((next_amt, steps + 1))
    return -1

_, money = map(int, input().split())
coins = list(map(int, input().split()))

print(coin_change(coins, money))