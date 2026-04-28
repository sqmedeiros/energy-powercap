import sys
input = sys.stdin.readline
print = sys.stdout.write
n, x = map(int,input().split())
a=list(map(int,input().split()))

dic = {}
if x == 1:
    print("IMPOSSIBLE")
    exit()
for i, el in enumerate(a):
    if x - el in dic:
        print(f'{dic[x-el]} {i + 1}')
        break

    dic[el] = i+1
else:
    print("IMPOSSIBLE")