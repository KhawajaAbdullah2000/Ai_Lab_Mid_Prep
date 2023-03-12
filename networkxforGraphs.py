import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

g=nx.Graph()
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)
g.add_node(8)
g.add_edge(5,3)
g.add_edge(5,7)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(7,8)
g.add_edge(4,8)

#print(g.nodes)
#print(g.edges)
#nx.draw(g)

# b=nx.all_neighbors(g,5)
# for i in b:
#     print(i)
    
# for a in g.nodes:
#     print(a)

# for a in g.edges:
#     print(a) #returns tuple for edges
edges = [
        ('S','A',1), ('S','G',10),
        ('A','B',2), ('A','C',1),
        ('B','D',5), ('C','D',3),
        ('C','G',4), ('D','G', 0),
      ]

graph = nx.DiGraph() #weighted graph
graph.add_weighted_edges_from(edges)

b=graph.successors('B') #can also use for predecessors
for i in b:
    print(i)

