n = int(input())
x = [int(i) for i in input().split()]
maxi = max(x)
suma = 0
for i in range(n):
    suma +=x[i]
    if(maxi<suma):
        maxi  = suma
    if(suma<0):
        suma = 0
print(maxi)