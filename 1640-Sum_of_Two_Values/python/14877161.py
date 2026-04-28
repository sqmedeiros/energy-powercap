n,x = map(int, input().split())
a = list(map(int, input().split()))
indexed = [(val, i + 1) for i, val in enumerate(a)]
indexed.sort(key=lambda z: z[0])
left, right = 0, len(a)-1
while(left < right):
    current_sum = indexed[left][0] + indexed[right][0]
    if(current_sum == x):
        print(indexed[right][1], indexed[left][1])
        exit()
    elif(current_sum < x):
        left+=1
    else:
        right-=1
print("IMPOSSIBLE")