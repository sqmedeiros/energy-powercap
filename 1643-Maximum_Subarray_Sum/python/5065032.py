from sys import stdin

stdin.readline()
array = list(map(int,stdin.readline().split()))

current = array[0]
best = current

for x in array[1:]:
    current = max(x, current + x)
    best = max(best, current)

print(best)