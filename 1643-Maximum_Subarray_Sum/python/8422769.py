qtd = int(input())
sequencia = [int(x) for x in input().split(" ")]

soma_maxima = float('-inf')  # inicia com o infinito negativo (menor valor real)
soma_atual = 0

for num in sequencia:
    soma_atual = max(num, soma_atual + num)
    soma_maxima = max(soma_maxima, soma_atual)

print(soma_maxima)