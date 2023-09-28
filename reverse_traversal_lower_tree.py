class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    if not root:
        return []
    queue = [root]
    stack = []
    result = []
    
    while queue:
        current = queue.pop(0)
        stack.append(current)
        
        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)
    
    while stack:
        result.append(stack.pop().data)
    return result