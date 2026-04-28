
def main():
    n = int(input())
    nums = list(map(int, input().split()))

    current = nums[0]
    best = nums[0]
    for i in range(1, n):

        if (current + nums[i] > nums[i]):
            current = current + nums[i]
        else: 
            current = nums[i]

        if (current > best):
            best = current



    print(best)
    return


main()

