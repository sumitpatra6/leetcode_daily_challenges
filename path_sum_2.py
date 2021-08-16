from tree_util import TreeNode, create_binary_tree_from_array

root = create_binary_tree_from_array([-2, None, -3])

def pathSum(root: TreeNode, targetSum: int):
        paths = []
        def topDown(head, total, path):
            if not head:
                return 
            print(path, head.val)
            total += head.val
            if head.left is None and head.right is None and total == targetSum:
                paths.append(path + [head.val])
                return
            # if total >= targetSum:
            #     return
            topDown(head.left, total, path + [head.val])
            topDown(head.right, total, path + [head.val])
            
                
        
        topDown(root, 0, [])
        return paths

r = pathSum(root, -5)
print(r)