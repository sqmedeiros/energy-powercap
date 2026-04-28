#! /usr/bin/env python3
# cses 1674 - Subordinates

class Node:
  def __init__(self, me):
    self.label = me
    self.adj   = []
    self.deg   = 0
    self.num   = 0
  def __repr__(self):
    return str(self.label)

#---#-- #---#-- #---#-- #---#-- #---#-- #---#--

n = int(input())
tree = {}
for k in range(1, n+1):
 tree[k] = Node(k)

k = 1
for a in map(int, input().split()):
  k += 1
  tree[k].adj.append( tree[a] )
  tree[a].deg += 1

t = []
for k in range(1, n+1):
  if tree[k].deg == 0:  t.append(tree[k])

while t:
  a = t.pop()
  for b in a.adj: 
    b.num += a.num + 1
    b.deg -= 1
    if b.deg == 0: t.append(b)

for k in range(1,n+1):
  print(tree[k].num, end=' ')
print()
