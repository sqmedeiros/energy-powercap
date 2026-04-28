n, t = map(int, input().split())

nums = list(map(int, input().split()))

dm = {}

for i in range(n - 1, -1, -1):  # Iterate from the last index
    for j in range(i - 1, -1, -1):  # Iterate from (i - 1) down to 0
        left = t - nums[i] - nums[j]
        if left in dm:  # Check if the required sum is in the hashmap
            print(j + 1, i + 1, dm[left][0], dm[left][1])
            exit()  # Terminate the program when a solution is found

    # Add pairs (nums[i] + nums[k]) to dm after checks are completed
    for k in range(i + 1, n):  # Iterate over indices after i
        dm[nums[i] + nums[k]] = (i + 1, k + 1)  # Store 1-based indices

print("IMPOSSIBLE")