# dp[s] = minima cantidad de monedas necesarias para sumar 's'
# si yo estoy considerando una moneda que vale 'k', entonces yo tengo algunas opciones:
#           * Yo puedo llegar a una suma s + k agregando esta moneda
#           * O puedo simplemente no agregar la moneda y seguir con una suma 's'

# estoy evaluando la moneda 'k' con suma 's':
#
#           dp[s+k] = min( dp[s+k] , dp[s] + 1 ) 


n, x = map(int, input().split())
inf = 10**7

coins = [int(x) for x in input().split()]


dp = [inf] * (x+1)
dp[0]=0

for k in coins: 
    for s in range((x+1) - k ): 
        dp[s+k] = min(dp[s+k], dp[s] + 1 )

if dp[x] == inf:
    print("-1")
else:
    print(dp[x])