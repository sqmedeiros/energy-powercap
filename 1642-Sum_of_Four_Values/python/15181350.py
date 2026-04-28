def main():
    n, x = map(int, input().split())
    a = []
    while len(a) < n:
        a.extend(map(int, input().split()))
    a = a[:n]

    # pairs_sum[s] = (i, j) avec i < j < b lors de l'usage
    pairs_sum = {}

    for b in range(n):
        # Cherche (i, j) < b et (b, a) > b tels que a[i]+a[j]+a[b]+a[a] = x
        for a_idx in range(b + 1, n):
            need = x - (a[b] + a[a_idx])
            if need in pairs_sum:
                i, j = pairs_sum[need]
                # i, j < b < a_idx  => indices distincts garantis
                print(i + 1, j + 1, b + 1, a_idx + 1)
                return
        # Après la recherche, on enregistre toutes les paires (i, b) pour i < b
        for i in range(b):
            s = a[i] + a[b]
            # Un seul couple par somme suffit (n'importe lequel)
            if s not in pairs_sum:
                pairs_sum[s] = (i, b)

    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()