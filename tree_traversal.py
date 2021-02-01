# Tree traversal in Python
"""
    1
   / \
  2   3
 / \
4   5

"""


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):
    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(23)
root.left.left = Node(6)
root.left.right = Node(17)
root.left.left.left = Node(5)
root.left.left.right = Node(8)
root.right.left = Node(18)
root.right.right = Node(25)
root.right.right.left = Node(24)
root.right.right.right = Node(29)




print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
