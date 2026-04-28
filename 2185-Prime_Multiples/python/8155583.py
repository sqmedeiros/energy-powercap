n, k, *a = [*map(int, open(0).read().split())]
N = 2**k
s = [1]+N*[0]
for i in range(k):
 s[2**i] = a[i]
A = 0
for i in range(1, k+1):
 B = 2**i-1
 o = 1
 while B<N:
  c = B& -B
  p = s[B] = s[B^c]*s[c]
  o &= p>=n
  A += n//p*(-1)**(i%2+1)
  r = B+c
  B = (((r^B)>>2)//c)|r
 if o: break
print(A)