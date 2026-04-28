s = int(input())
arr = [int(i) for i in input().split()]

soma = arr[0]
maximo = arr[0]

for i in range(1, s):
    soma = max(soma + arr[i], arr[i])
    maximo = max(soma, maximo)

print(maximo) 