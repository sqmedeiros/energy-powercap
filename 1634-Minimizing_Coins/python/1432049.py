from sys import stdin, stdout
n, x = map(int, stdin.readline().split())
c = sorted(list(map(int, stdin.readline().split())))
l = [1000001]*(x+1)
l[0] = 0
for y in range(1,x+1):
    for z in c:
        if z<=y:
            l[y] = min(l[y],l[y-z]+1)
        else:break
if l[x]==1000001:stdout.write('-1')
else:stdout.write(str(l[x]))