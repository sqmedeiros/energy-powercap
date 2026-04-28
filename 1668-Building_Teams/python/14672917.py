
from collections import defaultdict, deque


def main():

    b = list(map(int, (input().split())))
    num_stu = b[0]
    num_relation = b[1]
    adj_list = defaultdict(list)

    for i in range(num_relation):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    team = [0] * (num_stu + 1)
    flag = True

    for i in range(1, num_stu + 1):
        if not flag:
            break
        if team[i] == 0:
            q = deque([i])
            team[i] = 1

            while q:
                u = q.popleft()

                for v in adj_list[u]:
                    if team[v] == 0:
                        team[v] = 3 -team[u]
                        q.append(v)
                    elif team[v] == team[u]:
                        flag = False
                        break
                if not flag:
                    break

    if not flag:
        print("IMPOSSIBLE")
    else:
        print(*team[1:])

if __name__ == "__main__":
    main()