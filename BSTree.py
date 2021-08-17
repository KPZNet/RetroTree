class BSTNode :
	# Constructor to create a new node
	def __init__(self, key) :
		self.key = key
		self.left = None
		self.right = None

class BSTree:

	root = None

	# A utility function to do inorder traversal of BST
	def inorder(self):
		if self.root is not None:
			self.inorder(self.root.left)
			print(self.root.key)
			self.inorder(self.root.right)


	# A utility function to insert a
	# new node with given key in BST
	def insert(self, key):

		# If the tree is empty, return a new node
		if self.root is None:
			self.root = BSTNode(key)
			return self.root

		# Otherwise recur down the tree
		if key < self.root.key:
			self.root.left = self.insert(self.root.left, key)
		else:
			self.root.right = self.insert(self.root.right, key)

		# return the (unchanged) node pointer
		return self.root

	# Given a non-empty binary
	# search tree, return the node
	# with minum key value
	# found in that tree. Note that the
	# entire tree does not need to be searched


	def minValueNode(self):
		current = self.root

		# loop down to find the leftmost leaf
		while(current.left is not None):
			current = current.left

		return current

	# Given a binary search tree and a key, this function
	# delete the key and returns the new root


	def deleteNode(self, key):
		if self.root is None:
			return self.root
		if key < self.root.key:
			self.root.left = self.deleteNode(self.root.left, key)
		elif(key > self.root.key):
			self.root.right = self.deleteNode(self.root.right, key)
		else:
			if self.root.left is None:
				temp = self.root.right
				root = None
				return temp
			elif self.root.right is None:
				temp = self.root.left
				root = None
				return temp
			temp = self.minValueNode(self.root.right)
			self.root.key = temp.key
			self.root.right = self.deleteNode(self.root.right, temp.key)

		return self.root