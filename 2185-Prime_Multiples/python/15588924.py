n, k = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]

result = 0

def solve(i=0, curr=1, count = 0):
    global result
    global v
    if i == len(v):
        if count == 0: return
        num = n // curr
        if count % 2 != 0:
            result += num
        else:
            result -= num

    else:
        solve(i+1,curr*v[i],count + 1)
        solve(i+1,curr, count)

solve()

print(result)