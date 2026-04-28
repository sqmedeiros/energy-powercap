class dsf:
    def __init__(self, key):
        self.key = key
        self.parent = self

    def find(self, a):
        temp = a
        while temp.key != temp.parent.key:
            temp = temp.parent
        return temp

    def union(self, b):
        root_a = self.find(self)
        root_b = self.find(b)
        if root_a.key < root_b.key:
            root_b.parent = root_a
            return root_a
        else:
            root_a.parent = root_b
            return root_b

temp = input()
temp = temp.split()

n = int(temp[0])
m = int(temp[1])

keys = range(1, n+1)
ds = {i:dsf(i) for i in keys}

roads = []
for i in range(m):
    roads.append(tuple(int(j) for j in input().split()))
for i in roads:
    ds[i[0]].union(ds[i[1]])
res = []
for i in keys:
    if ds[i].find(ds[i]).key != 1:
        ds[1].union(ds[i])
        res.append(f"1 {i}")
print(len(res))
for i in res:
    print(i)