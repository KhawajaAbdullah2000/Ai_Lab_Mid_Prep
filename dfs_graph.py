
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


def dfs(visited,graph,root): #node is root
    if root not in visited:
        print(root,end=" ")
        visited.append(root)
    for n in graph[root]:
        dfs(visited,graph,n)
        
        

           
visited=[]
   
print("dfs of the graph is: ") 
dfs(visited,graph,'5') # 5 is root       


