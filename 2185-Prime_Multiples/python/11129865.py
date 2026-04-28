import itertools

def conta_multiplos(n, primos):
    resultado = 0
    k = len(primos)
    for i in range(1, k + 1):
        for combinacao in itertools.combinations(primos, i):
            lcm = 1
            for p in combinacao:
                lcm *= p
            if i % 2 == 1:  
                resultado += n // lcm
            else:  
                resultado -= n // lcm

    return resultado

# Input
n, k = map(int, input().split())  
primos = list(map(int, input().split()))  

# Output
resultado = conta_multiplos(n, primos)
print(resultado)