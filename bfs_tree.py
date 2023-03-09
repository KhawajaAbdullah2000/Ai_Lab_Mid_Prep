class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

n=Node(1)
n.left=Node(2)
n.right=Node(3)
n.left.left=Node(4)

#print(n.val,n.left.val,n.right.val,n.left.left.val)
#bfs
def bfs(root):
    queue=[]
    visited=[]
    queue.append(root)
    while(queue):
        node=queue.pop(0)
        visited.append(node.val) #our bfs path
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited
    
print(bfs(n))