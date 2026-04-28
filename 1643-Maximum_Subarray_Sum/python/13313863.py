import sys

n = int(sys.stdin.readline())
ll = list(map(int, sys.stdin.readline().split()))

mx = ll[0]
cm = 0

for val in ll:
    cm += val
    if cm > mx:
        mx = cm
    if cm < 0:
        cm = 0

print(mx)