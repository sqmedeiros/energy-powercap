import sys

# Leer la entrada
data = sys.stdin.read().splitlines()
if len(data) < 2:
    sys.exit()

s1 = data[0].strip()
s2 = data[1].strip()

n = len(s1)
m = len(s2)

# Inicializamos el vector dp
dp = list(range(m + 1))

# Calcular la distancia
for i in range(1, n + 1):
    new_dp = [i] + [0] * m
    for j in range(1, m + 1):
        cost = 0 if s1[i - 1] == s2[j - 1] else 1
        new_dp[j] = min(
            dp[j] + 1,          # eliminación
            new_dp[j - 1] + 1,  # inserción
            dp[j - 1] + cost    # reemplazo
        )
    dp = new_dp

# Imprimir el resultado final
print(dp[m])