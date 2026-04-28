n, m = list(map(int, input().split()))
friends = [[] for i in range(n)]
for i in range(m):
    pair = input().split()
    friends[int(pair[0]) - 1].append(int(pair[1]) - 1)
    friends[int(pair[1]) - 1].append(int(pair[0]) - 1)

teams = ["0"]*n
possible = True

for curr in range(n):
    if teams[curr] != "0":
        continue
    teams[curr] = "1"
    q = [curr]
    while len(q) > 0:
        pupil = q.pop(0)
        for friend in friends[pupil]:
            if teams[friend] != "0":
                if teams[friend] == teams[pupil]:
                    possible = False
                continue
            teams[friend] = "2" if teams[pupil] == "1" else "1"
            q.append(friend)

if possible:
    print(" ".join(teams))
else:
    print("IMPOSSIBLE")