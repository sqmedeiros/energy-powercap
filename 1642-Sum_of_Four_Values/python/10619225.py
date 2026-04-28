n,target=map(int,input().split())
nums=list(map(int,input().split()))
ans = []
def func(nums,target):
    # sort the given array:
    n=len(nums)
    dic={}
    for i in range(n):
        if nums[i] in dic:
            dic[nums[i]].append(i+1)
        else:
            dic[nums[i]]=[i+1]
    nums.sort()
    if n < 4 or nums[-1] + nums[-2] + nums[-3]+nums[-4] < target:
        return -1
    for i in range(n):
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    return [dic[nums[i]].pop(), dic[nums[j]].pop(), dic[nums[k]].pop(), dic[nums[l]].pop()]

                    k += 1
                    l -= 1

                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1

    return -1
ele=func(nums,target)
if ele==-1:
    print("IMPOSSIBLE")
else:
    for i in ele:
        print(i,end=" ")