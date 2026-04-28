n, x = map(int, input().split())
arr = list(map(int, input().split()))

d = dict()
d2 = dict()
for index, elem in enumerate(arr):
    d2[elem] = index+1

def check():
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            id34 = x - arr[i] - arr[j]
            if id34 in d:
                print(i+1, j+1, d[id34][0], d[id34][1])
                return True

        for k in range(i+1, n):
            d[arr[i]+arr[k]] = (i+1, k+1) 

    return False

def check2():
    pairs = [(arr[i], i+1) for i in range(n)]
    pairs.sort()

    left = 0
    right = n-1


    while left < right:
        _sum = pairs[left][0] + pairs[right][0]
        for i in range(left+1, right):
            _sum = pairs[i][0] + pairs[left][0] + pairs[right][0]
            if _sum >= x:
                right -=1
                break
            else:
                val = x-_sum
                if val in d2 and d2[val] not in {pairs[i][1], pairs[left][1], pairs[right][1]}:
                    print(pairs[left][1], pairs[right][1], pairs[i][1], d2[val])
                    return True
        else:
            left +=1
    return False

ans = check()
if not ans:
    print("IMPOSSIBLE")





