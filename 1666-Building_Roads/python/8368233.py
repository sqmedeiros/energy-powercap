rank = []

def get_rank(node):
    while(node != rank[node]):
        rank[node] = rank[rank[node]]
        node = rank[node]
    return node

def union(x, y):
    x = get_rank(x)
    y = get_rank(y)
    rank[x] = y

def main():
    global rank
    n, m = map(int, input().split())
    rank = [0]+[i+1 for i in range(n)]

    # print(rank)


    for _ in range(m):
        x, y = map(int, input().split())
        union(x,y)
    unique = set()
    for i in range(n):
        unique.add(get_rank(i+1))

    unique = list(unique)
    print(len(unique) -1)
    for i in range(1, len(unique)):
        print(unique[0], unique[i])

        # print(rank)

if __name__ == "__main__":
    main()