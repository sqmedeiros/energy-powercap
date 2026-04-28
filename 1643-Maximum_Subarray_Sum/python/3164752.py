# import sys

# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

n = int(input())
A = list(map(int,input().split(" ")))
c = g = A[0]
for i in range(1,n):
 c = max(c+A[i],A[i])
 g = max(c,g)
print(g)

# sys.stdin.close()
# sys.stdout.close()