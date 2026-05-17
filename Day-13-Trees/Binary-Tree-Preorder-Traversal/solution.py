class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return

        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(preorder_traversal(root))  # [1,2,3]