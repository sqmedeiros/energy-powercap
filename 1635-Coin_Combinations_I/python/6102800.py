# Entrada máxima
CONSTRAIN_INPUT = int(100)

# LIMITAÇÕES
CONSTRAIN = int(10e6)
MODULO = int(1e9 + 7)


def coin_comb(soma_desejada, moedas):
    solucoes = [0] * (soma_desejada + 1)
    solucoes[0] = 1

    for valor in range(soma_desejada + 1):
        if solucoes[valor] != 0:
            for moeda in moedas:
                if valor + moeda <= soma_desejada:
                    solucoes[valor + moeda] = (solucoes[valor + moeda] + solucoes[valor]) % MODULO

    return solucoes[soma_desejada]


line_1st = input()
line_2nd = input()

n, x = map(int, line_1st.split())
c = list(map(int, line_2nd.split()))
c.sort()

print(coin_comb(x, c))