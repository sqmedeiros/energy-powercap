n = int(input())
bosses = list(map(int, input().split()))

# Create adjacency list for subordinates
subordinates = [[] for _ in range(n+1)]
for i in range(n-1):
    employee = i + 2  # Employee IDs start from 2
    boss = bosses[i]
    subordinates[boss].append(employee)

# Initialize count array
count = [0] * (n+1)

# Process nodes in a way that guarantees we've processed all children before parents
# This is essentially a topological sort in reverse
def count_subordinates():
    # First identify all leaf nodes (employees with no subordinates)
    stack = []
    for i in range(1, n+1):
        if not subordinates[i]:  # If employee has no subordinates
            stack.append(i)

    # Process nodes from leaves up to the root
    processed = [False] * (n+1)
    remaining_children = [len(subordinates[i]) for i in range(n+1)]

    while stack:
        employee = stack.pop()
        processed[employee] = True

        # If not the root (employee 1), update the boss's count
        if employee > 1:
            boss = bosses[employee-2]  # Adjust index for bosses array
            count[boss] += 1 + count[employee]  # Add this employee + all their subordinates

            # Decrease remaining children count for the boss
            remaining_children[boss] -= 1

            # If we've processed all children of the boss, add boss to stack
            if remaining_children[boss] == 0 and not processed[boss]:
                stack.append(boss)

count_subordinates()
print(*count[1:])