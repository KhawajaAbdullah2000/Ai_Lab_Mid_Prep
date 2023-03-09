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
def dfs(root):
    if root:
        print(root.val)
        dfs(root.left)
        dfs(root.right)
    

dfs(n)