def soma(left, right):

    left_soma = float("inf") * -1
    temp = 0
    for x in left[::-1]:
        temp += x
        left_soma = max(temp, left_soma)

    right_soma = float("inf") * -1
    temp2 = 0
    for x in right:
        temp2 += x
        right_soma = max(temp2, right_soma)


    return left_soma + right_soma

def split(lista):
    if len(lista) == 1:
        return lista[0]

    mid = len(lista)//2
    left = lista[0:mid]
    right = lista[mid:]

    n_left = split(left)
    n_right = split(right)
    mid = soma(left, right)

    return max(n_left, n_right, mid)

n = int(input())

lista = list(map(int, input().split()))
max_soma = split(lista)

print(max_soma)