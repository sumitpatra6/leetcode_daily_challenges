from utils.tree_util import create_binary_tree_from_array, inorder, TreeNode
from pprint import pprint

def maxProduct(root: TreeNode):
    # populate sum_map
    memory = {}
    def sum(head: TreeNode):
        if not head:
            return 0
        l = sum(head.left)
        r = sum(head.right)
        current = l + r + head.val
        memory[head] = current
        return current
    sum(root)
    pprint(memory)
    answer = float('-inf')
    total = memory[root]
    print(total)
    def get_max(head):
        if not head:
            return

        nonlocal answer
        if head.left:
            answer = max(answer, memory[head.left]*(total - memory[head.left]))
        if head.right:
            answer = max(answer, memory[head.right] * (total - memory[head.right]))
        get_max(head.left)
        get_max(head.right)
    get_max(root)
    return answer


root = create_binary_tree_from_array([1,1])
result = maxProduct(root)
print(result)