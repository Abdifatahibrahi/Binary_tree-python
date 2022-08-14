from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))
tree.add(Node(5))

print(tree.head)
print(tree.head.left)
print(tree.head.right)

