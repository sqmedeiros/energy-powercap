a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

if n > m:
    a, b = b, a
    n, m = m, n

prev = list(range(n + 1))
curr = [0] * (n + 1)

for j in range(1, m + 1):
    curr[0] = j
    for i in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            curr[i] = prev[i - 1]
        else:
            curr[i] = 1 + min(
                prev[i],      
                curr[i - 1],   
                prev[i - 1]    
            )
    prev, curr = curr, prev

print(prev[n])