"""
{1,2,0,3}
Output:
4
Explanation:
    1
   / \
  2   0
 /
3
0-1-2-3
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    
def consecutive2(root: TreeNode):
    global_max = float('-inf')
    def find_length(root: TreeNode):
        if not root:
            return []
        left = find_length(root.left)
        right = find_length(root.right)
        current = root.val
        if left:
            if len(left) == 1 and abs(left[0] - current) == 1:
                left.append(current)
            elif left[0] > left[-1] and left[-1] - current == -1:
                left.append(current)
            elif left[0] < left[-1] and left[-1] - current == 1:
                left.append(current)
            
        if right:
            if len(right) == 1 and abs(current - right[0]) == 1:
                right = [current] + right
            elif right[0] > right[-1] and current - right[0] == 1:
                right = [current] + right
            elif right[0] < right[-1] and current - right[0] == -1:
                right = [current] + right
        joined_chain = []
        if left[-1] == right[0]:
            joined_chain = left + right[1:]
        if 






root = TreeNode(1)
node_2 = TreeNode(2)
node_0 = TreeNode(0)
node_3 = TreeNode(3)
root.left = node_2
root.right = node_0
node_2.left = node_3