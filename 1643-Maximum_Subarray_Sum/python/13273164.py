_ = int(input())
lista = list(map(int,input().split()))
soma_atual = lista[0]
soma_maxima = lista[0]
for i in range(1, len(lista)):
    elemento = lista[i]
    soma_atual = max(elemento, soma_atual + elemento)
    soma_maxima = max(soma_maxima, soma_atual)
print(soma_maxima)