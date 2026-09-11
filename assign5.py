class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

node1 = Node(50)
node2 = Node(60)
node3 = Node(10)
node4 = Node(20)
node5 = Node(15)

# Recursive
def insert(root,key):
    if root is None:
        return Node(key)
    
    if root.data == key:
        return root
    
    if root.data < key:
        root.right = insert(root.right,key)
    
    else:
        root.left = insert(root.left,key)
    
    return root

root = Node(50)
root = insert(root,60)
root = insert(root,10)
root = insert(root,20)
root = insert(root,15)
