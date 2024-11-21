class Node:
    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self._insert(root.left, data)
        elif data > root.item:
            root.right = self._insert(root.right, data)
        return root

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None or root.item == data:
            return root
        elif data < root.item:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root is not None:
            self._inorder(root.left, result)
            result.append(root.item)
            self._inorder(root.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root is not None:
            result.append(root.item)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root is not None:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.item)

bst = BST()

values = [10, 50, 40, 70, 30, 90, 20]
for value in values:
    bst.insert(value)


print("Inorder traversal of the BST:", bst.inorder())
print("Search for no. 40",bst.search(40))
print("Postorder traversal of the BST  is:", bst.postorder())