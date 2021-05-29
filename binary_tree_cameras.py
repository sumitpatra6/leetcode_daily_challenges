class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(0)
node_0 = TreeNode(0)
node_1 = TreeNode()
node_2 = TreeNode()
root.left = node_0
node_0.left = node_1
node_0.right = node_2

def minCameraCover(root):
    def count(node, previous_covered):
        if not node:
            return 0
        if not previous_covered:
            return 1 + count(node.left, True) + count(node.right, True)
        else:
            return count(node.left, False) + count(node.right, False)                                   
    return min(1+count(root.left, True) + count(root.right, True),count(root.left, False) + count(root.right, False))

result = minCameraCover(root)
print(result)
