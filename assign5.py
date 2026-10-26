class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def h(n): # gets the height
    return n.height if n else 0

def update(n): # update the height
    n.height = 1 + max(h(n.left), h(n.right))

def balance(n): # finding balancing factor
    return h(n.left) - h(n.right)

# Right Rotation
def rotate_right(y):
    x = y.left
    y.left, x.right = x.right, y
    update(y); update(x)
    return x

# Left Rotation
def rotate_left(x):
    y = x.right
    x.right, y.left = y.left, x
    update(x); update(y)
    return y

# Insert elements in bst
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    # Update the tree factors after insertion
    update(root)
    b = balance(root)
    # perform AVL rotations
    if b > 1:                            # left heavy
          if key > root.left.key:          # LR case
              root.left = rotate_left(root.left)
          return rotate_right(root)
    if b < -1:                           # right heavy
          if key < root.right.key:         # RL case
              root.right = rotate_right(root.right)
          return rotate_left(root)
    return root
def postorder_predecessor(root, key):
    cur, candidate = root, None
    while cur:
        if key < cur.key:
            cur = cur.left
        elif key > cur.key:
            if cur.left:                 # left sibling subtree root
                candidate = cur.left
            cur = cur.right
        else:                            # found the node
            if cur.right:
                return cur.right.key
            if cur.left:
                return cur.left.key
            return candidate.key if candidate else None
    return None

# Postorder printing
def postorder(root, out):
    if root:
        postorder(root.left, out)
        postorder(root.right, out)
        out.append(root.key)
    return out



# Checking 
root = None
for k in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, k)
print("Postorder:", postorder(root, []))   # [20, 40, 30, 60, 80, 70, 50]
for k in [50, 70, 60, 40, 20]:
    print(f"pred({k}) =", postorder_predecessor(root, k))
