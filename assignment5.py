class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def h(n): return n.height if n else 0
def upd(n): n.height = 1 + max(h(n.left), h(n.right))
def bal(n): return h(n.left) - h(n.right)

def rot_right(y):
    x = y.left
    y.left, x.right = x.right, y
    upd(y); upd(x)
    return x

def rot_left(x):
    y = x.right
    x.right, y.left = y.left, x
    upd(x); upd(y)
    return y

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # ignore duplicates
    upd(root)
    b = bal(root)
    if b > 1:                       # left heavy
        if bal(root.left) < 0:
            root.left = rot_left(root.left)
        return rot_right(root)
    if b < -1:                      # right heavy
        if bal(root.right) > 0:
            root.right = rot_right(root.right)
        return rot_left(root)
    return root

def postorder_predecessor(root, key):
    """Return the key of the post-order predecessor, or None."""
    cand, cur = None, root
    while cur and cur.key != key:
        if key < cur.key:
            cur = cur.left
        else:
            if cur.left:            # went right at an ancestor with a left child
                cand = cur.left
            cur = cur.right
    if not cur:
        return None                 # key not in tree
    if cur.right: return cur.right.key
    if cur.left:  return cur.left.key
    return cand.key if cand else None

# ---- demo ----
def postorder(n, out):
    if n:
        postorder(n.left, out); postorder(n.right, out); out.append(n.key)
    return out

if __name__ == "__main__":
    root = None
    for k in [50, 30, 70, 20, 40, 60, 80, 35, 45, 65]:
        root = insert(root, k)

    order = postorder(root, [])
    print("Post-order:", order)
    for k in order:
        print(f"pred({k}) = {postorder_predecessor(root, k)}")