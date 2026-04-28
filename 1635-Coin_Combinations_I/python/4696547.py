qpoe,wanted = map(int,input().split())
coins = list(map(int,input().split()))
ways = [0 for x in range(wanted)]
for y in coins:
  if y <= wanted:
      ways[y-1] = 1

#print(ways)

for x in range(wanted):
    cur_pos = ways[x]
    if cur_pos != 0:
        for y in coins:
            if x+y < wanted:
                ways[x+y] = (ways[x+y]+cur_pos)%(10**9+7)

print(ways[-1])