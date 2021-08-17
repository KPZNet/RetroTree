class BSTNode :
	# Constructor to create a new node
	def __init__(self, key) :
		self.key = key
		self.left = None
		self.right = None

class BSTree:

	root = None

	# A utility function to do inorder traversal of BST
	def __inorder(self, node):
		if node is not None:
			self.inorder(node.left)
			print(node.key)
			self.inorder(node.right)

	def inorder(self):
		self._BSTree__inorder(self.root)

	# A utility function to insert a
	# new node with given key in BST
	def __insert(self, node, key):

		if node is None:
			return BSTNode(key)

		# Otherwise recur down the tree
		if key < node.key:
			node.left = self._BSTree__insert(node.left, key)
		else:
			node.right = self._BSTree__insert(node.right, key)

		# return the (unchanged) node pointer
		return node

	def insert(self, key):
		self.root = self._BSTree__insert(self.root, key)
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


	# Given a binary search tree and a key, this function
	# delete the key and returns the new root


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
			temp = self.minValueNode(node.right)
			node.key = temp.key
			node.right = self._BSTree__deleteNode(node.right, temp.key)

		return node

	def deleteNode(self, key):
		return self._BSTree__deleteNode(self.root, key)