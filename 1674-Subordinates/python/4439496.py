n = int(input())
nums = [int(i) for i in input().split(" ")]

# n = 10
# nums = [1,2,3,4,5,6,7,8,9]

class Node:
    def __init__(self,number):
        self.number = number
        self.children = []
        self.local_children_count = 0
        self.parent = None

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def set_parent(self,parent):
        self.parent = parent
        self.parent.children.append(self)

    def traverse(self):
        stack = []
        stack = [self]
        children = []
        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)
                children.append(child)

        while children:  
            node = children.pop()
            if(node.parent):
                node.parent.local_children_count+= (1+node.local_children_count)

emps = [Node(i+1) for i in range(n)]

for i in range(1,n):
    emps[i].set_parent(emps[nums[i-1]-1])

emps[0].traverse()
print(' ' .join([str(i.local_children_count) for i in emps]))