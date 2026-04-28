s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

# Criar matriz DP
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Casos base
for i in range(n + 1):
    dp[i][0] = i  # Remover todos de s1

for j in range(m + 1):
    dp[0][j] = j  # Adicionar todos de s2

# Preencher matriz
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i-1] == s2[j-1]:
            # Caracteres iguais - não precisa operação
            dp[i][j] = dp[i-1][j-1]
        else:
            # Escolher mínimo entre as 3 operações
            dp[i][j] = 1 + min(
                dp[i-1][j],    # Remover de s1
                dp[i][j-1],    # Adicionar em s1
                dp[i-1][j-1]   # Substituir
            )

print(dp[n][m])