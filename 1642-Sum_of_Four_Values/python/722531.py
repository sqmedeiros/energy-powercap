from collections import *
def isValid(e1, e2):
    if e1[0] == e2[0] or e1[0] == e2[1] or e1[1] == e2[0] or e1[1] == e2[1]:
        return False
    return True
def getAns(nums, target):
    sums = defaultdict(list)
    sumVal = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sums[nums[i]+nums[j]].append((i+1, j+1))
            if target - (nums[i]+nums[j]) in sums:
                sumVal.add(target - (nums[i]+nums[j]))
    for num in sumVal:
        for e1 in sums[num]:
            for e2 in sums[target-num]:
                if isValid(e1, e2):
                    return '%d %d %d %d'%(e1[0], e1[1], e2[0], e2[1])
    return 'IMPOSSIBLE'


def main():
    [_, target] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(getAns(nums, target))
main()