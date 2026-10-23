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

# Path Searching
def search_path(root,val):
    path = []
    curr = root
    
    while curr is not None:
        path.append(curr.data)
        
        if val == curr.data:
            return path
        elif val < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    return path

# Finding the least Common Ancestor
def find_lca(root,n1,n2):
    arr1 = []
    arr2 = []
    arr1 = search_path(root,n1)
    arr2 = search_path(root,n2)
    l3 = []
    i = 0
    j = 0
    while i < len(arr1) and j<len(arr2):
        if arr1[i] != arr2[j]:
            break
        l3.append(arr1[i])
        i += 1
        j += 1
    if l3:
        return l3[-1]
    else:
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
