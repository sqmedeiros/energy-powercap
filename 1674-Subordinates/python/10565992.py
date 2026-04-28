def count_subordinates(n, bosses):
    # 1. lépés: Szomszédsági lista létrehozása a fa struktúrához
    tree = [[] for _ in range(n + 1)]

    for employee in range(2, n + 1):
        boss = bosses[employee - 2]
        tree[boss].append(employee)

    # 2. lépés: Beosztottak számát tároló lista inicializálása
    subordinates_count = [0] * (n + 1)

    # 3. lépés: Iteratív DFS a beosztottak számának kiszámítására
    stack = [1]  # A főigazgatótól (1-es alkalmazott) indulunk
    post_order = []

    while stack:
        employee = stack.pop()
        post_order.append(employee)  # Az alkalmazottot később dolgozzuk fel
        for subordinate in tree[employee]:
            stack.append(subordinate)

    # A beosztottak számának kiszámítása post-order bejárással
    while post_order:
        employee = post_order.pop()
        count = 0
        for subordinate in tree[employee]:
            count += subordinates_count[subordinate] + 1  # Számoljuk a beosztottakat
        subordinates_count[employee] = count

    # A beosztottak számának kiírása (1-től n-ig)
    return subordinates_count[1:]

# Bemenet olvasása
n = int(input())
bosses = list(map(int, input().split()))

# A beosztottak számának kiszámítása minden alkalmazottra
result = count_subordinates(n, bosses)

# Eredmény kiírása
print(" ".join(map(str, result)))