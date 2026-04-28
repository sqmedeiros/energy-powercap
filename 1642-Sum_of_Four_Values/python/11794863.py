from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # Number of elements
    x = int(data[1])  # Target sum
    v = list(map(int, data[2:]))  # Input numbers

    # HashMap to store pair sums
    hm = {}

    for i in range(n - 1, -1, -1):  # Iterate from the last element
        for j in range(i - 1, -1, -1):  # Iterate from (i - 1) down to 0
            idx = x - v[i] - v[j]  # Calculate the required value to complete the sum
            if idx in hm:  # Check if the complement is in the hashmap
                print(i + 1, j + 1, hm[idx][0] + 1, hm[idx][1] + 1)
                return

        # Add pairs (v[i] + v[j]) to the hashmap for later checks
        for j in range(i + 1, n):  # Iterate from (i + 1) to (n - 1)
            hm[v[i] + v[j]] = (i, j)

    # If no solution is found
    print("IMPOSSIBLE")

# Call the function to solve the problem
if __name__ == "__main__":
    solve()