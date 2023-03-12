import networkx as nx
import matplotlib.pyplot as plot
from queue import PriorityQueue
from queue import Queue
class node:
    def __init__(self,state, parent=None, move=None):
        self.state=state
        self.parent=parent
        self.move=move
    
    
    
    def expand(self):
        nodes=[]
        i,j = self.state.index(0)//3, self.state.index(0)%3
        if i>0:
            new_state=self.state[:]
            new_state[(i-1)*3+j], new_state[(3*i)+j]= new_state[(3*i)+j], new_state[(i-1)*3+j]
            nodes.append(node(new_state,self,'up'))
        if i<2:
            new_state=self.state[:]
            new_state[(i+1)*3+j],new_state[(3*i)+j]= new_state[(3*i)+j] , new_state[3*(i+1)+j]
            nodes.append(node(new_state,self,'down'))
        if j>0:
            new_state=self.state[:]
            new_state[(3*i)+j-1] , new_state[(3*i)+j]=new_state[(3*i)+j],new_state[(3*i)+j-1]       
            nodes.append(node(new_state,self,'left'))
        if j<2:
            new_state=self.state[:]
            new_state[(3*i)+j+1] , new_state[(3*i)+j]=new_state[(3*i)+j],new_state[(3*i)+j+1]       
            nodes.append(node(new_state,self,'right'))
        return nodes    

def bfs(start,goal):
    start_node= node(start)
    queue=Queue()
    queue.put(start_node)
    visited=set()
    while queue:
        n = queue.get(0)
        if n.state == goal:
            return get_path(n)
        visited.add(tuple(n.state))

        for child in n.expand():
            if tuple(child.state) not in visited:
                queue.put(child)    

def dfs(start,goal):
    start_node= node(start)
    stack=[start_node]
    visited=set()
    while stack:
        n= stack.pop()
        if n.state==goal:
            return get_path(n)
        visited.add(tuple(n.state))
        for child in n.expand():
            if tuple(child.state) not in visited:
                stack.append(child)
            
     

def get_path(object):
        path=[]
        while object.parent:
            path.append(object.move)
            object= object.parent
        path.reverse()
        return path       
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#print(tuple(initial_state))
print(bfs(initial_state,goal_state)) 
print('\n',dfs(initial_state,goal_state))              