n=input()
l=list(map(int,input().split()))
s=h=l[0]
for i in l[1:]:
    h=max(i,h+i)
    s=max(h,s)
print(s)