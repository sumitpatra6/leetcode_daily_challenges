from utils.tree_util import create_binary_tree_from_array, inorder


def good_nodes(root):
    count = 0
    def util(head, max_till_now):
        if not head:
            return
        nonlocal count
        if head.val >= max_till_now:
            count += 1
            max_till_now = head.val
        util(head.left, max_till_now)
        util(head.right, max_till_now)
    util(root, float('-inf'))
    return count

array =  [3,1,4,3,None,1,5]
root = create_binary_tree_from_array(array)
print('--')
result = good_nodes(root)
print(result)
