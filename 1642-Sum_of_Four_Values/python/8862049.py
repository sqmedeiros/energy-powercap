nx = input().split()
n = int(nx[0])
x = int(nx[1])
a = list(map(int, input().split()))

# Usaremos un diccionario para almacenar las sumas parciales
# La clave será la suma y el valor será una lista de pares de índices
partial_sums = {}

for i in range(n):
    for j in range(i + 1, n):
        current_sum = a[i] + a[j]
        if x - current_sum in partial_sums:
            for idx_pair in partial_sums[x - current_sum]:
                idx1, idx2 = idx_pair
                # Asegurarse de que los índices sean diferentes
                if idx1 != i and idx1 != j and idx2 != i and idx2 != j:
                    print(idx1 + 1, idx2 + 1, i + 1, j + 1)
                    exit()
        if current_sum not in partial_sums:
            partial_sums[current_sum] = []
        partial_sums[current_sum].append((i, j))

print("IMPOSSIBLE")