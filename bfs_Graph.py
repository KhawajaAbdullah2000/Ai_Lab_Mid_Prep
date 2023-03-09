
graph = {
'5':['3','7'],
'3':['2','4'],
'7':['8'],
'2':[],
'4':['8'],
'8':[]
}
# for i,k in graph.items():
#     print(i,'edges',k)


def bfs(visited,graph,node): #node is root
    queue=[]    
    visited.append(node)
    queue.append(node)
    while(queue):
       m= queue.pop(0)# get 0th index or head of queue 
       print(m,end=" ")
       for n in graph[m]: 
           if n not in visited:
               visited.append(n)
               queue.append(n)
           
visited=[]
   
print("bfs of the graph is: ") 
bfs(visited,graph,'5') # 5 is root       


