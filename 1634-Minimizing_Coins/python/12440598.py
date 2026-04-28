from collections import deque

n, x = map(int, input().split())
coins = list(map(int, input().split()))

valid_coins = [c for c in coins if c <= x]
if not valid_coins:
    print(-1)
    exit()

valid_coins.sort(reverse=True)

max_sum = x
visited = [False] * (max_sum + 1)
visited[0] = True
dist = [0] * (max_sum + 1)

queue = deque([0])
found = False

while queue:
    current = queue.popleft()
    if current == x:
        found = True
        break
    for coin in valid_coins:
        next_sum = current + coin
        if next_sum > x:
            continue
        if not visited[next_sum]:
            visited[next_sum] = True
            dist[next_sum] = dist[current] + 1
            if next_sum == x:
                found = True
                queue.clear()
                break
            queue.append(next_sum)
    if found:
        break

print(dist[x] if found else -1)