import sys
sys.setrecursionlimit(10**6)

n = int(input())

sub = [[] for _ in range(n+1)]
l = list(map(int,input().split()))
for i in range(len(l)):
    sub[l[i]].append(i+2)

res= [0]*(n+1)
def solve(sub,index):
    if len(sub[index]) == 0:
        return 0
    ans = len(sub[index])

    for i in sub[index]:
        ans = ans+ solve(sub,i)
    res[index] = ans
    return ans

solve(sub,1)
print(*res[1:])
