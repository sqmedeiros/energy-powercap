n, x = map(int, input().split())
a = list(map(int, input().split()))

def sum_two_values(n,x,a):
    if x == 1:
        if 0 not in a or x not in a:
            return "IMPOSSIBLE"
    positions = {}
    for i in range(n):
        diff = x - a[i]
        if diff in positions:
            return f"{positions[diff]} {i+1}"
        positions[a[i]] = i+1

    return "IMPOSSIBLE"

print(sum_two_values(n,x,a))