class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,data):
    if root is None:
        return Node(data)

    if root.val > data :
        root.left = insert(root.left,data)

    else:
        root.right = insert(root.right,data)

    return root

def inorder(root,arr):
    if arr is None:
        arr = []

    if root:
        inorder(root.left,arr)
        arr.append(root.val)
        inorder(root.right,arr)
    return arr

def convert_to_min_heap(arr,i):
    if i >= len(arr):
        return None

    node = Node(arr[i])
    node.left = convert_to_min_heap(arr,2*i+1)
    node.right = convert_to_min_heap(arr,2*i+2)
    return node

def level_order(root):
    if root is None:
        return None

    queue = [root]

    while queue:
        next_level = []
        for n in queue:
            print(str(n.val),end=" ")
        print()
        for n in queue:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        queue = next_level

root = None
for v in [4, 2, 6, 1, 3, 5, 7]:
    root = insert(root, v) 

arr = inorder(root,[])
heap_root = convert_to_min_heap(arr,0)
level_order(heap_root)
