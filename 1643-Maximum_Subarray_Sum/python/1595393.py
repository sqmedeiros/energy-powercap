n = eval(input())
x = list(map(int, input().split()))
x_psums = [0]
for i in range(n):
    x_psums.append(x[i] + x_psums[i])

b = 0
max_sum = None
for a in range(1, len(x_psums)):
    if x_psums[a-1] < x_psums[b]:
        b = a - 1
    sum = x_psums[a] - x_psums[b]
    if max_sum == None:
        max_sum = sum
    else:
        if sum > max_sum:
            max_sum = sum

print(max_sum)