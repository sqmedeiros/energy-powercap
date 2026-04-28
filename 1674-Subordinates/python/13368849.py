class Worker:
    def __init__(self, p):
        self.parent = p
        self.children = 0

worker_count = int(input())
workers = [Worker(-1) for _ in range(worker_count)]

def subtract(index):
    return index - 1
worker_assigner = 1

levels = {0: 0}
for boss in map(subtract, map(int, input().split())):
    workers[worker_assigner].parent = boss
    workers[boss].children += 1
    worker_assigner += 1

leaves = []
for leaf in range(worker_count):
    if(workers[leaf].children == 0):
        leaves.append(leaf)

leaf_index = 0
while(leaf_index < worker_count and workers[leaves[leaf_index]].parent >= 0):
    levels[workers[leaves[leaf_index]].parent] = levels.get(workers[leaves[leaf_index]].parent, 0) + levels.setdefault(leaves[leaf_index], 0) + 1
    workers[workers[leaves[leaf_index]].parent].children -= 1
    if(workers[workers[leaves[leaf_index]].parent].children == 0):
        leaves.append(workers[leaves[leaf_index]].parent)
    leaf_index += 1
display_index = 0
while((display_index + 1) < worker_count):
    print(levels[display_index], end = ' ')
    display_index += 1
print(levels[worker_count - 1])