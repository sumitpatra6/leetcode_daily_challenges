from typing import List
class TreeNode(object):
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

get_left = lambda x: 2*x + 1
get_right = lambda x: 2*x + 2

def create_binary_tree_from_array(array: List) -> TreeNode:
    def util(array:List, index: int) -> TreeNode:
        if index >= len(array):
            return None
        if array[index] == None:
            return None
        node = TreeNode(array[index])
        node.left = util(array, get_left(index))
        node.right = util(array, get_right(index))
        return node
    return util(array, 0)

def inorder(root: TreeNode) -> None:
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

######### test
array = [-2, None, -3]
root = create_binary_tree_from_array(array)
inorder(root)