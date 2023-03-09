graph={
    '0':[('1',2),('3',5)],
    '1':[('2',4),('3',5),('6',1)],
    '2':[('4',4),('5',6)],
    '3':[('4',2),('6',6)],
    '4':[('5',3),('6',7)],
    '5':[('6',3)],
    '6':[] #goal
}

def path_cost(path):
    total_cost=0
    for (node,cost) in path:
        total_cost+=cost
    return total_cost,path[-1][0] # path[-1][0] meanslast node in the path

def ucs(graph,start,goal):
    visited=[]
    queue=[ [(start,0)] ]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop() #choose first element which was also now least cost     
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if (node==goal):
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)

solution=ucs(graph,'0','6')
print("Solution is: ",solution)
print("cost of saolutiuon is: ",path_cost(solution)[0])