from utils.tree_util import create_binary_tree_from_array, inorder


def findtarget(root, k):
    complement_set = set()
    def util(head):
        if not head:
            return  False
        current = head.val
        if current in complement_set:
            return True
        else:
            complement_set.add(k - current)
        return util(head.left) or util(head.right)

    return util(root)



root = create_binary_tree_from_array([2,1,3])

result = findtarget(root, 4)
print(result)