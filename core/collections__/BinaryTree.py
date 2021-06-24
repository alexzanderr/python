

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


    def preorder(self, start: Node, traversal=""):
        """ root => left => right"""
        if start:
            traversal += str(start.data) + "->"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal


    def inorder(self, start: Node, traversal=""):
        """ left => root => right"""
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.data) + "->"
            traversal = self.inorder(start.right, traversal)
        return traversal


    def postorder(self, start: Node, traversal=""):
        """ left => right => root"""
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.data) + "->"
        return traversal


# TESTING
if __name__ == '__main__':
    tree = BinaryTree(51)
    tree.root.left = Node(12)
    tree.root.right = Node(43)
    tree.root.left.left = Node(19)
    tree.root.left.right = Node(89)
    result = tree.preorder(tree.root)
    print(result)
    result = tree.inorder(tree.root)
    print(result)
    result = tree.postorder(tree.root)
    print(result)