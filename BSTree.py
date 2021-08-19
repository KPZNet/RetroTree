import copy

class BSTNode :
	# Constructor to create a new node
	def __init__(self, key, payload=None) :
		self.key = key
		self.payload = payload
		if payload == None:
			self.payload = key
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.key)

class BSTree:

	root = None
	COUNT = [10]

	def __init__(self, _root=None):
		if _root != None:
			self.root = _root


	# A utility function to insert a
	# new node with given key in BST
	def __insert(self, node, key, payload=None):

		if node is None:
			return BSTNode(key, payload)

		# Otherwise recur down the tree
		if key < node.key:
			node.left = self._BSTree__insert(node.left, key, payload)
		else:
			node.right = self._BSTree__insert(node.right, key, payload)

		# return the (unchanged) node pointer
		return node

	def insert(self, key, payload=None):
		self.root = self._BSTree__insert(self.root, key, payload)
		return self.root

	# Given a non-empty binary
	# search tree, return the node
	# with minum key value
	# found in that tree. Note that the
	# entire tree does not need to be searched

	def __minValueNode(self, node):
		current = node

		# loop down to find the leftmost leaf
		while (current.left is not None):
			current = current.left

		return current

	# Given a non-empty binary
	# search tree, return the node
	# with minum key value
	# found in that tree. Note that the
	# entire tree does not need to be searched

	def minValueNode(self):
		return self._BSTree__minValueNode(self.root)


	def __deleteNode(self, node, key):
		if node is None:
			return node
		if key < node.key:
			node.left = self._BSTree__deleteNode(node.left, key)
		elif(key > node.key):
			node.right = self._BSTree__deleteNode(node.right, key)
		else:
			if node.left is None:
				temp = node.right
				node = None
				return temp
			elif node.right is None:
				temp = node.left
				node = None
				return temp
			temp = self._BSTree__minValueNode(node.right)
			node.key = temp.key
			node.right = self._BSTree__deleteNode(node.right, temp.key)

		return node

	def deleteNode(self, key):
		return self._BSTree__deleteNode(self.root, key)

	# Function to print binary tree in 2D
	# It does reverse inorder traversal
	def __print2DUtil(self, root, space) :
		# Base case
		if (root == None) :
			return

		# Increase distance between levels
		space += self.COUNT[0]

		# Process right child first
		self._BSTree__print2DUtil ( root.right, space )

		# Print current node after space
		# count
		print ()
		for i in range ( self.COUNT[0], space ) :
			print ( end=" " )
		print ( root.key )

		# Process left child
		self._BSTree__print2DUtil ( root.left, space )


	def print_tree(self, val="key", left="left", right="right"):
		def display(root, val=val, left=left, right=right):
			"""Returns list of strings, width, height, and horizontal coordinate of the root."""
			# No child.
			if getattr(root, right) is None and getattr(root, left) is None:
				line = '%s' % getattr(root, val)
				width = len(line)
				height = 1
				middle = width // 2
				return [line], width, height, middle

			# Only left child.
			if getattr(root, right) is None:
				lines, n, p, x = display(getattr(root, left))
				s = '%s' % getattr(root, val)
				u = len(s)
				first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
				second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
				shifted_lines = [line + u * ' ' for line in lines]
				return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

			# Only right child.
			if getattr(root, left) is None:
				lines, n, p, x = display(getattr(root, right))
				s = '%s' % getattr(root, val)
				u = len(s)
				first_line = s + x * '_' + (n - x) * ' '
				second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
				shifted_lines = [u * ' ' + line for line in lines]
				return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

			# Two children.
			left, n, p, x = display(getattr(root, left))
			right, m, q, y = display(getattr(root, right))
			s = '%s' % getattr(root, val)
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
			second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
			if p < q:
				left += [n * ' '] * (q - p)
			elif q < p:
				right += [m * ' '] * (p - q)
			zipped_lines = zip(left, right)
			lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
			return lines, n + m + u, max(p, q) + 2, n + u // 2

		lines, *_ = display(self.root, val, left, right)
		print("\n")
		for line in lines:
			print(line)
		print("\n")

	# This function traverse the skewed binary tree and
	# stores its nodes pointers in vector nodes[]
	def storeBSTNodes(self, root, nodes):
		# Base case
		if not root:
			return

		# Store nodes in Inorder (which is sorted
		# order for BST)
		self.storeBSTNodes(root.left, nodes)
		nodes.append(root)
		self.storeBSTNodes(root.right, nodes)

	# Recursive function to construct binary tree
	def buildTreeUtil(self, nodes, start, end):
		# base case
		if start > end:
			return None

		# Get the middle element and make it root
		mid = (start + end) // 2
		node = nodes[mid]

		node.left = self.buildTreeUtil(nodes, start, mid - 1)
		node.right = self.buildTreeUtil(nodes, mid + 1, end)
		return node

	# This functions converts an unbalanced BST to
	# a balanced BST
	def rebalance(self):
		# Store nodes of given BST in sorted order
		nodes = []
		self.storeBSTNodes(self.root, nodes)

		n = len(nodes)
		self.root = self.buildTreeUtil(nodes, 0, n - 1)

	# A utility function to do inorder traversal of BST
	def __inorder(self, node, d):
		if node is not None:
			self._BSTree__inorder(node.left, d)
			d.append(copy.deepcopy(node))
			self._BSTree__inorder(node.right, d)

	def inorder(self):
		d = []
		self._BSTree__inorder(self.root, d)
		return d


	def __preOrder(self, node, d) :
		if not node :
			return
		d.append(copy.deepcopy(node))
		self._BSTree__preOrder ( node.left, d )
		self._BSTree__preOrder ( node.right, d )

	def preOrder(self):
		d =[]
		self._BSTree__preOrder(self.root, d)
		return d


	def __search(self, node, key) :
		if node == None :
			return False

		elif node.key == key :
			return node.payload
		elif node.key < key :
			return self._BSTree__search ( node.right, key )
		else :
			return self._BSTree__search ( node.left, key )

	def search(self, key):
		return self._BSTree__search ( self.root, key )

	
	# function to find max value less then N
	def __findMaxforN(self, node, key):
		
		# Base cases
		if node == None:
			return -1
		if node.key == key:
			return key
	
		# If root's value is smaller, try in
		# right subtree
		elif node.key < key:
			k = self._BSTree__findMaxforN( node.right, key )
			if k == -1:
				return node.key
			else:
				return k
	
		# If root's key is greater, return
		# value from left subtree.
		elif node.key > key:
			return self._BSTree__findMaxforN( node.left, key )
	
	def findmax(self, key):
		return self._BSTree__findMaxforN(self.root, key)

	def copytree(self) :
		bst = BSTree()
		nodes = self.preOrder ()
		for n in nodes :
			bst.insert(n.key, n.payload)
		return bst