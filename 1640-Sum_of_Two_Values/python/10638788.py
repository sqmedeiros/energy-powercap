def find_two_sum(n, x, arr):
    # Create a list of tuples (value, original_index)
    indexed_arr = [(arr[i], i + 1) for i in range(n)]  # +1 for 1-based indexing

    # Sort the array based on the values
    indexed_arr.sort()

    # Initialize two pointers
    left = 0
    right = n - 1

    # Iterate using the two-pointer technique
    while left < right:
        current_sum = indexed_arr[left][0] + indexed_arr[right][0]

        # Check if the current sum equals the target sum x
        if current_sum == x:
            # Return the original indices
            return indexed_arr[left][1], indexed_arr[right][1]
        elif current_sum < x:
            # Move the left pointer to the right to increase the sum
            left += 1
        else:
            # Move the right pointer to the left to decrease the sum
            right -= 1

    # If no pair is found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

# Input reading
n, x = map(int, input().split())  # Read n and x
arr = list(map(int, input().split()))  # Read the array

# Call the function and get the result
result = find_two_sum(n, x, arr)

# Print the result
if result == "IMPOSSIBLE":
    print(result)
else:
    print(result[0], result[1])