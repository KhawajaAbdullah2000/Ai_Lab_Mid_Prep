class Path:
  def __init__(self, *args):
    if len(args) == 1:
      self.nodes = [ args[0] ]
      self.cost = cost[ args[0] ]

    elif len(args) == 2:
      self.nodes = list(args[0])
      self.cost = args[1]
  
  def __str__(self):
    return f'{self.nodes} : {self.cost}'

  def last(self):
    last_index = len(self.nodes) - 1
    return self.nodes[last_index]
  
  def move(self, node, weight):
    self.cost -= cost[self.last()]
    self.cost += weight + cost[node]
    self.nodes.append(node)
  
  def copy(self):
    return Path(self.nodes, self.cost)

def a_search(graph, root, target):
  paths = [ Path(root) ]
  
  while paths:
    path = cheapest_path(paths)
    paths.remove(path)
    node = path.last()
   
    if node == target:
      return path

    for n in graph.neighbors(node):
      weight = graph[node][n]['weight']
      new_path = path.copy()
      new_path.move(n, weight)
      paths.append(new_path)
      print(new_path)
    print()
  return []

def cheapest_path(paths):
  min = paths[0]
  for p in paths:
    if p.cost < min.cost:
      min = p
  return min

import networkx as nx

cost = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 0, 'G': 6}
edges = [
        ('S','A',1), ('S','G',10),
        ('A','B',2), ('A','C',1),
        ('B','D',5), ('C','D',3),
        ('C','G',4), ('D','G', 0),
      ]

graph = nx.DiGraph()
graph.add_weighted_edges_from(edges)

traversal = a_search(graph, 'S', 'D')
print('traversal:', traversal)