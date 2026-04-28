i1 = int(input())
i2 = input()

i2 = [int(i) for i in i2.split()]

maior = i2[0]
soma = 0

for i in i2:
    soma = max(i, soma+i)
    maior = max(maior, soma)

print(maior)