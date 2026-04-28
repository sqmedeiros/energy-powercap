"""!
 \doxy
 \Collection  CSES
 \Problem  1669
 \Title   Round Trip
 \Description Cycle in a graph
 \Algorithm  Graph visit
 \Complexity  Linear time and space
 \Status   Accapted
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

def visit(G, s, seen, p): 
 S = [s]
 while len(S) > 0:
  u = S.pop()
  seen[u] = True
  for v in G[u]:
   if v == p[u]: continue # skip immediate backlinks
   if not seen[v]:
    S.append(v)
    p[v] = u
   else: # proper cycle found
    cyc = []
    w = u
    cyc.append(v)
    cyc.append(w)
    while w != v: 
     w = p[w]
     cyc.append(w)
    return cyc
 return None

def find_cycle(G):
 g = len(G)
 seen = g * [False]
 p = g * [-1]
 for u in G.nodes():
  if not seen[u]: 
   cyc = visit(G, u, seen, p)
   if cyc is not None: return cyc
 return None

def main():
 n, m = [int(s) for s in input().split()]
 G = graph(n, 1)
 for _ in range(m):
  u, v = [int(s) for s in input().split()]
  G.add_edge(u, v)
 cyc = find_cycle(G)
 if cyc is None:
  print('IMPOSSIBLE')
 else:
  print(len(cyc))
  for u in cyc:
   print(u, end=' ')
  print()

if __name__ == "__main__": main()