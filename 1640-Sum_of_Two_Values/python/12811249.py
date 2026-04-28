import sys
N, X = map(int, input().split())
data = [(int(x), index) for index, x in enumerate(input().split())]
data.sort()

left = 0
right = N-1


while left < right:
    if data[left][0] + data[right][0] < X:
        left += 1
    elif data[left][0] + data[right][0] > X:
        right -= 1
    else:
        print(data[left][1]+1, data[right][1]+1)
        sys.exit(0)

print("IMPOSSIBLE")