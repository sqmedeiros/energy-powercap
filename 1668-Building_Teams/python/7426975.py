import sys
from collections import defaultdict

sys.setrecursionlimit(2*(10**5))  # Ajustăm limita maximă a adâncimii recursivității

def dfs(nod, echipa_curent):
    # Parcurgem vecinii nodului curent
    for prieten in graf[nod]:
        # Verificam daca prietenul are aceeasi echipa cu nodul curent
        if dare_echipa[prieten] == echipa_curent:
            # Daca da, afisam "IMPOSSIBLE" si inchidem programul
            print("IMPOSSIBLE")
            sys.exit(0)
        # Verificam daca prietenul nu are echipa data
        if dare_echipa[prieten] == 0:
            # Dam prietenului echipa opusa celei a nodului curent
            dare_echipa[prieten] = 3 - echipa_curent
            # Aplicam recursiv functia dfs pentru a parcurge mai departe graful
            dfs(prieten, 3 - echipa_curent)

# Citim valoarea lui n si m de la tastatura
n, m = map(int, input().split())
# Initializam un dictionar cu listă de prieteni pentru a reprezenta graful
graf = defaultdict(list)
# Inițializăm o listă pentru a ține la echipă fac parte elevii
dare_echipa = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graf[a].append(b)
    graf[b].append(a)

for i in range(1, n + 1):
    if dare_echipa[i] == 0:
        dare_echipa[i] = 1
        dfs(i, 1)

print(" ".join(str(dare_echipa[i]) for i in range(1, n + 1)))