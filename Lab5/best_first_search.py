def gbfs(graph, root, target):
  closed = [root]
  opened   = list(graph.neighbors(root))
  
  while opened:
    print('closed:', closed)
    print('opened:', opened)
    print()

    node = cheapest_node(opened)
    opened.remove(node)
    closed.append(node)

    if node == target:
      return closed

    opened.extend(graph.neighbors(node))
  
  return []

def cheapest_node(nodes):
  min = nodes[0]
  for n in nodes:
    if cost[n] < cost[min]:
      min = n
  return min

import networkx as nx

cost = {'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'H': 0, 'I': 9, 'S': 13, 'G': 4}
edges = [
        ('S','A',3), ('S','B',2),
        ('A','C',4), ('A','D',1),
        ('B','E',3), ('B','F',1),
        ('E','H',5), ('F','I',2), ('F','G',0),
      ]

graph = nx.DiGraph()
graph.add_weighted_edges_from(edges)

traversal = gbfs(graph, 'S', 'H')
print('traversal:', traversal)