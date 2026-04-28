n = int(input())
direct_bosses = list(map(int, input().split()))

subordinates = [[] for _ in range(n+1)]
for emp, boss in enumerate(direct_bosses, start=2):
    subordinates[boss].append(emp)

count = [0] * (n+1)

stack = [(1, 0)]  # (employee, state), state 0 = pre-processing
visited = [0] * (n+1)

while stack:
    emp, state = stack.pop()
    if state == 0:
        # Push the same employee back with state=1 to process after children
        stack.append((emp, 1))
        for sub in subordinates[emp]:
            stack.append((sub, 0))
    else:
        # Post-processing: all children counts are ready
        total = 0
        for sub in subordinates[emp]:
            total += 1 + count[sub]
        count[emp] = total

print(*count[1:])