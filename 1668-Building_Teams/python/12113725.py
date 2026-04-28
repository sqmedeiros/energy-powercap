from collections import deque

#Los adyacentes seran de equipos opuestos a su padre
people, connections = map(int, input().split())
adj = {i: [] for i in range(1, people + 1)}

for _ in range(connections):
    inicio, final = map(int, input().split())
    adj[inicio].append(final)
    adj[final].append(inicio)


equipos = [-1] * (people + 1) #equipo de cada persona

def bfs(start):
    queue = deque([start])
    equipos[start] = 1  #  primer nodo  equipo 1

    while queue:
        node = queue.popleft()
        current = equipos[node]
        opuesto = 2 if current == 1 else 1  #cambiar equipo

        for vecino in adj[node]:
            if equipos[vecino] == -1:  
                equipos[vecino] = opuesto
                queue.append(vecino)
            elif equipos[vecino] == current: 
                return False
    return True

# Hacer un for pues no todos los nodos estan desconectados
possible = True
for i in range(1, people + 1):
    if equipos[i] == -1:  #no visitado
        if not bfs(i):
            possible = False
            break

# Imprimir resultado
if possible:
    print(" ".join(map(str, equipos[1:])))
else:
    print("IMPOSSIBLE")