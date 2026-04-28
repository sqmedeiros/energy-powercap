n, m = map(int, input().split())

graf = [[] for _ in range(n)]
echipa = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graf[a - 1].append(b - 1)
    graf[b - 1].append(a - 1)

def atribuie_echipe():
    for start_node in range(n):
        if echipa[start_node] != 0:
            continue
        echipa[start_node] = 1
        stack = [start_node]
        while stack:
            node = stack.pop()
            current_team = echipa[node]
            next_team = 3 - current_team
            for neighbor in graf[node]:
                if echipa[neighbor] == current_team:
                    print("IMPOSSIBLE")
                    exit()
                if echipa[neighbor] == 0:
                    echipa[neighbor] = next_team
                    stack.append(neighbor)

atribuie_echipe()

# Afișează asignarea echipelor pentru fiecare elev
print(" ".join(map(str, echipa)))