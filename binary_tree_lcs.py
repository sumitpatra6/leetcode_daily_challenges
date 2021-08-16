class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

def longestConsecutive(root):
    global_maximum = []
    def inorder(root, max_till_now):
        nonlocal global_maximum
        print(max_till_now)
        if not root:
            return
        current = root.val
        if not max_till_now:
            max_till_now.append(current)
        elif current == max_till_now[-1] + 1:
            max_till_now.append(current)
        elif len(max_till_now) >= len(global_maximum):
            global_maximum = max_till_now[:]
            max_till_now = [current]
        else:
            max_till_now = []

        inorder(root.left, max_till_now)
        inorder(root.right, max_till_now)
        if len(max_till_now) >= len(global_maximum):
            global_maximum = max_till_now[:]
    inorder(root, [])
    print("-----")
    print(global_maximum)




def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = TreeNode(1)
node_3 = TreeNode(3)
node_2 = TreeNode(2)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
root.right = node_3
node_3.left = node_2
node_3.right = node_4
node_4.right = node_5


longestConsecutive(root)



