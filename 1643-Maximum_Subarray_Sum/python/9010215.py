# Read input
n = int(input())
array = list(map(int, input().split()))

# Initialize variables
max_sum = array[0]
current_sum = array[0]

# Iterate through the array starting from the second element
for i in range(1, n):
    # Calculate the current sum of the subarray ending at the current position
    current_sum = max(array[i], current_sum + array[i])
    # Update the maximum sum found so far
    max_sum = max(max_sum, current_sum)

# Output the maximum subarray sum
print(max_sum)