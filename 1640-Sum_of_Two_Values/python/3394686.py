n,m = map(int, input().split())
s = list(map(int, input().split()))

x = dict()

for i in range(len(s)):
    num = s[i]
    value = m-num
    if num in x:
        print(x[num]+1,i+1)
    else:
        x[value]=i
print("IMPOSSIBLE")
