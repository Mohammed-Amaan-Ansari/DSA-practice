class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(max_depth(root))  # 3