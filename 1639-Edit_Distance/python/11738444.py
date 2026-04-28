first = input()
second = input()

n = len(first)
m = len(second)

# inicializada com zeros, esta matriz (tamanho n+1 X m+1) será usada para armazenar os custos de edição
dp = []
for i in range(n + 1):
    dp.append([0] * (m + 1))

# preenche a primeira coluna com o custo de remover i caracteres 
for i in range(n + 1):
    dp[i][0] = i
# preenche a primeira linha com o custo de inserir j caracteres
for j in range(m + 1):
    dp[0][j] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # se os caracteres são iguais, o custo é o mesmo que o custo de edição das substrings anteriores 
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # caso contrário, o custo é o (mínimo entre os custos de inserir, remover ou substituir) + 1 da edição 
        else:
            cost_insert = dp[i][j - 1]
            cost_remove = dp[i - 1][j]
            cost_replace = dp[i - 1][j - 1]
            dp[i][j] = min(cost_insert, cost_remove, cost_replace) + 1

# o custo de edição da string é o valor na última célula da matriz
print(dp[n][m])
