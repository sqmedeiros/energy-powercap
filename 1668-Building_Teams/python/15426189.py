import sys
from collections import deque


def solve():
    """
    Meghatározza, hogy a diákok két csapatba oszthatók-e barátsági korlátok nélkül,
    és ha igen, kiírja a beosztást. A beosztást BFS-szel ellenőrzi.
    """
    try:
        # A nagy bemeneti méret miatt gyorsabb beolvasást használunk
        data = sys.stdin.read().split()
        if not data:
            return

        N = int(data[0])  # Diákok száma
        M = int(data[1])  # Barátságok száma

        # Szomszédsági lista építése
        adj = [[] for _ in range(N + 1)]

        data_index = 2
        for _ in range(M):
            u = int(data[data_index])
            v = int(data[data_index + 1])
            adj[u].append(v)
            adj[v].append(u)
            data_index += 2

    except Exception:
        # Hiba a beolvasás során
        print("IMPOSSIBLE")
        return

    # A csapatok tömbje: 0 = nincs csapatban, 1 = 1-es csapat, 2 = 2-es csapat
    team = [0] * (N + 1)

    # Bejárás minden diákra (független komponensekre is)
    for i in range(1, N + 1):
        # Ha a diák még nincs csapatban, indítunk egy BFS-t
        if team[i] == 0:
            queue = deque([i])
            team[i] = 1  # Kezdetben 1-es csapat

            while queue:
                u = queue.popleft()
                current_team = team[u]
                next_team = 3 - current_team  # Váltás a másik csapatra (1->2, 2->1)

                for v in adj[u]:
                    if team[v] == 0:
                        # Ha a szomszéd még nincs csapatban, hozzárendeljük az ellenkező csapatot
                        team[v] = next_team
                        queue.append(v)
                    elif team[v] == current_team:
                        # Konfliktus: két barát ugyanabban a csapatban van.
                        print("IMPOSSIBLE")
                        return

    # Ha az összes diákot csapatba tudtuk sorolni konfliktus nélkül
    # Kiírjuk az eredményt, kihagyva az 0 indexet
    print(*(team[1:]))


if __name__ == "__main__":
    solve()