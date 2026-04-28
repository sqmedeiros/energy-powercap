import sys

def read_ints():
    return [int(i) for i in sys.stdin.readline().strip().split()]

def read_int():
    return int(sys.stdin.readline().strip())

n, x = read_ints()
nums = read_ints()

sums_max = {} # max (i, j), i < j, that gives this sum
sums_min = {} # min (i, j), i > j, that gives this sum

for i in range(n):
    for j in range(i + 1, n):
        sums_max[nums[i] + nums[j]] = (i, j)
for i in reversed(range(n)):
    for j in reversed(range(i)):
        sums_min[nums[i] + nums[j]] = (i, j)

#print(sums_min)
#print(sums_max)

for s, (i, j) in sums_min.items():
    target = x - s
    s2 = sums_max.get(target)
    if s2 is not None:
        k, l = s2
        if i < k:
            print(i + 1, j + 1, k + 1, l + 1)
            break
else:
    print("IMPOSSIBLE")


