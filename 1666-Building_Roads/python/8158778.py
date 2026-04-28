# Building Roads

def union_find(N, M, connections):
    ds = [-1 for _ in range(N + 1)]
    ans = []

    def find(u):
        if ds[u] < 0:
            return u
        ds[u] = find(ds[u])
        return ds[u]

    def merge(u, v):
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if ds[u] < ds[v]:
            u, v = v, u
        ds[v] += ds[u]
        ds[u] = v
        return True

    # Process each connection
    for a, b in connections:
        merge(a, b)

    # Find additional connections required
    for i in range(1, N):
        if merge(i, i + 1):
            ans.append((i, i + 1))

    return len(ans), ans

# Test the function with the provided test case
# Accepting input from the user for N and M
N, M = map(int, input().split())

# Accepting input for the connections
connections = [tuple(map(int, input().split())) for i in range(M)]

# Calling the function with the input data
num_connections, additional_connections = union_find(N, M, connections)

# Printing the results
print(num_connections)
for a, b in additional_connections:
    print(f"{a} {b}")