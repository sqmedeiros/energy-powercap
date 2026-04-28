def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))

n = read()
arr = readlist()
ans = arr[0]
curr = arr[0]
s = 0
for i in range(1,len(arr)):
    curr+=arr[i]
    if curr<arr[i]:
        curr=arr[i]
    if ans < curr:
        ans = curr

print(ans)