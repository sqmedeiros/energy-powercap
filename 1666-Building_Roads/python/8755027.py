"""
 \doxy
 \Collection  CSES
 \Problem  1666
 \Title   Building Roads
 \Description Connected Components
 \Algorithm  Graph visit
 \Complexity  Linear time and space
 \Status   
"""
# tag::graph[]
class graph(list):
 def __init__(G, n, start=0):
  "Construct the empty graph on n nodes, with nodes start .. start+n-1"
  G.extend([[] for _ in range(start + n)]) # G is a list of lists of nodes
  G.start = start

 def nodes(G):
  "Return the nodes of G as a range"
  return range(G.start, len(G))

 def add_node(G):
  "Add a new node to G and return its index"
  v = len(G)
  G.append([])
  return v

 def add_arc(G, u, v):
  "Add arc (u, v) to G"
  G[u].append(v)

 def add_edge(G, u, v):
  "Add edge [u, v] to G"
  G[u].append(v)
  G[v].append(u)
# end::graph[]

# tag::visit[]
def visit(G, s, seen): 
 """Yields all nodes u reachable from s in G, 
 marking them visited using boolean array seen"""
 S = [s] # O(n) extra space
 seen[s] = True
 while len(S) > 0:
  u = S.pop()
  yield u
  for v in G[u]:
   if not seen[v]:
    S.append(v)
    seen[v] = True
# end::visit[]

# tag::cc[]
def cc(G):
 """Return (R, leader) where:
  -- R is the list of CC representatives (in increasing order)
  -- leader[u] == r if the CC representative of node u is node r"""
 g = len(G)
 leader = g * [-1]
 seen = g * [False]
 R = []
 for u in G.nodes():
  if leader[u] == -1:
   for v in visit(G, u, seen):
    leader[v] = u
   R.append(u)
 return (R, leader)
# end::cc[]

def main():
 n, m = [int(s) for s in input().split()]
 G = graph(n, 1)
 for _ in range(m):
  u, v = [int(s) for s in input().split()]
  G.add_edge(u, v)
 R, leader = cc(G)
 print(len(R) - 1)
 for i, u in enumerate(R):
  if i < len(R)-1:
   print(u, R[i+1])

if __name__ == "__main__": main()