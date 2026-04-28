# Source: https://usaco.guide/general/io
# def binSearch(a, b, e):

def binSearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid][0] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid][0] > x:
            return binSearch(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binSearch(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

N, x = map(int, input().split())
a = list(map(int, input().split()))
a = [(value, index) for index, value in enumerate(a)]
a.sort()
# print(a)
succ = 0
for ind in range(N):
#     if ind + 1 == N and succ == 0: 
#         print("IMPOSSIBLE")
#         break
    index_val, index_ind = a[ind]
    rem = x - index_val
    remind = binSearch(a, ind+1, N-1, rem)
#     print(rem, remind, a[ind+1:])
    if  remind != -1:
        remind_val, remind_ind = a[remind]
        print(min(index_ind + 1, remind_ind + 1), max(index_ind + 1, remind_ind + 1))

        succ = 1
        break
    # else:
    #     print("IMPOSSIBLE")
    #     break
#         f = ao.index(a[ind])
#         if x == 2*ao[f]:
#             print(f + 1, ao.index(a[remind + 1], f+1)+1)
#         else:
#             print(f + 1, ao.index(a[remind + 1])+1)
#         succ = 1
#         break

if succ == 0:
    print("IMPOSSIBLE")