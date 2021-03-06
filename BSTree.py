class BSTNode:

    # Constructor to create a new node
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        if payload == None:
            self.payload = key
        self.left = None
        self.right = None

    def __str__(self):
        return str (self.key)


class BSTree:
    root = None

    def __str__(self):
        return self.print_tree()

    def __init__(self, _root=None):
        if _root != None:
            self.root = _root

    def copyme(self):
        bst = BSTree()
        nds = self.preOrder()
        for n in nds:
            bst.insert(n.key, n.payload)
        return bst

    def insert(self, key, payload=None):

        def __insert(node, key, payload=None):

            if node is None:
                return BSTNode (key, payload)

            if key == node.key:
                return node

            # Otherwise recur down the tree
            if key < node.key:
                node.left = __insert (node.left, key, payload)
            else:
                node.right = __insert (node.right, key, payload)

            # return the (unchanged) node pointer
            return node

        self.root = __insert (self.root, key, payload)
        return self.root

    def get_min_value_node(self, node):
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    def delete(self, key):

        def __deleteNode(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = __deleteNode (node.left, key)
            elif (key > node.key):
                node.right = __deleteNode (node.right, key)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                temp = self.get_min_value_node (node.right)
                node.key = temp.key
                node.payload = temp.payload
                node.right = __deleteNode (node.right, temp.key)

            return node
        self.root = __deleteNode (self.root, key)
        return self.root

    COUNT = [10]

    def __print2DUtil(self, root, space):
        # Base case
        if (root == None):
            return

        space += self.COUNT[0]

        self._BSTree__print2DUtil (root.right, space)

        print ()
        for i in range (self.COUNT[0], space):
            print (end=" ")
        print (root.key)

        self._BSTree__print2DUtil (root.left, space)

    def print_tree(self, title="BST", val="key", left="left", right="right"):

        def display(root, val=val, left=left, right=right):
            if getattr (root, right) is None and getattr (root, left) is None:
                line = '%s' % getattr (root, val)
                width = len (line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            if getattr (root, right) is None:
                lines, n, p, x = display (getattr (root, left))
                s = '%s' % getattr (root, val)
                u = len (s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            if getattr (root, left) is None:
                lines, n, p, x = display (getattr (root, right))
                s = '%s' % getattr (root, val)
                u = len (s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            left, n, p, x = display (getattr (root, left))
            right, m, q, y = display (getattr (root, right))
            s = '%s' % getattr (root, val)
            u = len (s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip (left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max (p, q) + 2, n + u // 2

        if self.root is None:
            return
        lines, *_ = display (self.root, val, left, right)
        print(title)
        for line in lines:
            print (line)

    def rebalance(self):

        def storeBSTNodes(root, nodes):
            if not root:
                return
            storeBSTNodes (root.left, nodes)
            nodes.append (root)
            storeBSTNodes (root.right, nodes)

        def buildTreeUtil(nodes, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = nodes[mid]

            node.left = buildTreeUtil (nodes, start, mid - 1)
            node.right = buildTreeUtil (nodes, mid + 1, end)
            return node

        nodes = []
        storeBSTNodes (self.root, nodes)

        n = len (nodes)
        self.root = buildTreeUtil (nodes, 0, n - 1)

    def inorder(self):

        def __inorder(node, d):
            if node is not None:
                __inorder (node.left, d)
                d.append (node)
                __inorder (node.right, d)

        d = []
        __inorder (self.root, d)
        return [i.payload for i in d]

    def inorderLessThanEqual(self, kValue):

        def __inorderLessThanEqual(node, d, kValue):
            if node is not None:
                __inorderLessThanEqual (node.left, d, kValue)
                if node.key <= kValue:
                    d.append (node)
                else:
                    return
                __inorderLessThanEqual (node.right, d, kValue)

        d = []
        __inorderLessThanEqual (self.root, d, kValue)
        return [i.payload for i in d]

    def inorderGreaterThanEqual(self, kValue):

        def __inorderGreaterThan(node, d, kValue):
            if node is not None:
                __inorderGreaterThan (node.left, d, kValue)
                if node.key >= kValue:
                    d.append (node)
                __inorderGreaterThan (node.right, d, kValue)

        d = []
        __inorderGreaterThan (self.root, d, kValue)
        return [i.payload for i in d]

    def inorderGreaterThan(self, kValue):

        def __inorderGreaterThan(node, d, kValue):
            if node is not None:
                __inorderGreaterThan (node.left, d, kValue)
                if node.key > kValue:
                    d.append (node)
                __inorderGreaterThan (node.right, d, kValue)

        d = []
        __inorderGreaterThan (self.root, d, kValue)
        return [i.payload for i in d]

    def inorder_between(self, kValue, end_value):

        def __inorderGreaterThan(node, d, kValue):
            if node is not None:
                __inorderGreaterThan (node.left, d, kValue)
                if node.key >= kValue and node.key <= end_value:
                    d.append (node)
                __inorderGreaterThan (node.right, d, kValue)

        d = []
        __inorderGreaterThan (self.root, d, kValue)
        return [i.payload for i in d]


    def preOrder(self):

        def __preOrder(node, d):
            if not node:
                return
            d.append (node)
            __preOrder (node.left, d)
            __preOrder (node.right, d)

        d = []
        __preOrder (self.root, d)
        return d

    def search(self, key):

        def __search(node, key):
            if node == None:
                return None

            elif node.key == key:
                return node.payload
            elif node.key < key:
                return __search (node.right, key)
            else:
                return __search (node.left, key)

        return __search (self.root, key)

    def get_key_for_time(self, key):

        def __findMaxforN(root, N):
            # Base cases
            if root == None:
                return -1
            if root.key == N:
                return N

            # If root's value is smaller, try in
            # right subtree
            elif root.key < N:
                k = __findMaxforN (root.right, N)
                if k == -1:
                    return root.key
                else:
                    return k

            # If root's key is greater, return
            # value from left subtree.
            elif root.key > N:
                return __findMaxforN (root.left, N)

        return __findMaxforN(self.root, key)

    def getsmallestkey(self):

        def get_smallest(root):
            if root != None:
                temp = root
                while temp.left != None:
                    temp = temp.left
                return temp.key

        return get_smallest(self.root)

    def getlargestkey(self):

        def get_largest(root):
            if root != None:
                temp = root
                while temp.right != None:
                    temp = temp.right
                return temp.key

        return get_largest(self.root)

    def get_latest_node_payload(self):
        k = self.getlargestkey()
        if k != None:
            return self.search(k)
        return None
    
