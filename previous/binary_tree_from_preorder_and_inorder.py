class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    preorder_index = 0
    def array_to_tree(left, right):
        if left > right:
            return None
        nonlocal preorder_index
        root_val = preorder[preorder_index]
        root = TreeNode(root_val)
        preorder_index += 1
        root.left = array_to_tree(left, inorder_index[root_val] - 1)
        root.right = array_to_tree(inorder_index[root_val] + 1, right)
        return root

    # build a inorder index
    inorder_index = {}
    print(inorder)
    for index, value in enumerate(inorder):
        inorder_index[value] = index

    print(inorder_index)
    return array_to_tree(0, len(preorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder, inorder)

print(root)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

inorder(root)