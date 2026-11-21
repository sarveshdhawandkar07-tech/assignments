# Node creation
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# BST creation
def insert(root,val):
    new_node = Node(val)
    if root is None:
        root = new_node
        return root
    
    if root.data > val:
        root.left = insert(root.left,val)
    
    else:
        root.right = insert(root.right,val)
        
    return root

# Finding the least common ancestor
def LCA(root,n1,n2):
    while root:
        if n1 < root.data and n2 < root.data:
            root = root.left
        elif n1 > root.data and n2 > root.data:
            root = root.right
        else:
            return root.data
    return None

# Main Function
root = None
root = insert(root,40)
root = insert(root,25)
root = insert(root,27)
root = insert(root,26)
root = insert(root,15)
root = insert(root,50)
root = insert(root,60)

print(find_lca(root,25,50))    
