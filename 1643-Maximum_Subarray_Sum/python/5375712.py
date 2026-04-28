n = int(input())
arr = [int(i) for i in input().split()]

pref = [0]*(n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + arr[i - 1]

min_l = (0, pref[0])
max_sum = pref[1] - pref[0]
for r in range(1, n + 1):
    summ = pref[r] - pref[min_l[0]]
    if summ > max_sum:
        max_sum = summ        
    if pref[r] < min_l[1]:
        min_l = r, pref[r]
print(max_sum)