# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree

from BSTree import BSTree

class Node:


	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key)
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a non-empty binary
# search tree, return the node
# with minum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):
	if root is None:
		return root
	if key < root.key:
		root.left = deleteNode(root.left, key)
	elif(key > root.key):
		root.right = deleteNode(root.right, key)
	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp
		elif root.right is None:
			temp = root.left
			root = None
			return temp
		temp = minValueNode(root.right)
		root.key = temp.key
		root.right = deleteNode(root.right, temp.key)

	return root

COUNT = [10]

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :
	# Base case
	if (root == None) :
		return

	# Increase distance between levels
	space += COUNT[0]

	# Process right child first
	print2DUtil ( root.right, space )

	# Print current node after space
	# count
	print ()
	for i in range ( COUNT[0], space ) :
		print ( end=" " )
	print ( root.key )

	# Process left child
	print2DUtil ( root.left, space )


# Wrapper over print2DUtil()
def print2D(root) :
	# space=[0]
	# Pass initial space count as 0
	print2DUtil ( root, 0 )


def print_tree(root, val="val", left="left", right="right"):
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

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)




# This function traverse the skewed binary tree and
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root, nodes) :
	# Base case
	if not root :
		return

	# Store nodes in Inorder (which is sorted
	# order for BST)
	storeBSTNodes ( root.left, nodes )
	nodes.append ( root )
	storeBSTNodes ( root.right, nodes )


# Recursive function to construct binary tree
def buildTreeUtil(nodes, start, end) :
	# base case
	if start > end :
		return None

	# Get the middle element and make it root
	mid = (start + end) // 2
	node = nodes[mid]

	# Using index in Inorder traversal, construct
	# left and right subtress
	node.left = buildTreeUtil ( nodes, start, mid - 1 )
	node.right = buildTreeUtil ( nodes, mid + 1, end )
	return node


# This functions converts an unbalanced BST to
# a balanced BST
def build_balanced_tree(root) :
	# Store nodes of given BST in sorted order
	nodes = []
	storeBSTNodes ( root, nodes )

	# Constucts BST from nodes[]
	n = len ( nodes )
	return buildTreeUtil ( nodes, 0, n - 1 )


# Function to do preorder traversal of tree
def preOrder(root) :
	if not root :
		return
	print ( "{} ".format ( root.data ), end="" )
	preOrder ( root.left )
	preOrder ( root.right )






# Driver code
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """


nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
bst = BSTree()
for num in nums:
	bst.insert(num)

bst.print_tree( "key", "left", "right" )

bst.deleteNode(19)
bst.deleteNode(12)
bst.deleteNode(6)

bst.print_tree( "key", "left", "right" )
r = build_balanced_tree( bst.root )
bst = BSTree(r)
bst.print_tree( "key", "left", "right" )

exit(0)

nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
root = None
for num in nums:
	root=insert(root,num)

print_tree(root, "key", "left", "right" )




rooty = None
rooty = insert(rooty, 50)
root = insert(rooty, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 100)
root = insert(root, 5)
root = insert(root, 45)
root = insert(root, 55)
root = insert(root, 25)
root = insert(root, 35)
root = insert(root, 90)
root = insert(root, 88)
root = insert(root, 12)
root = insert(root, 41)
root = insert(root, 14)
root = insert(root, 74)
root = insert(root, 23)
root = insert(root, 2)
root = insert(root, 39)
root = insert(root, 17)


print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
#root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
#root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
#root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

print('Tree Print')
#print2D(root)

print_tree(root, "key", "left", "right" )
root = build_balanced_tree( root )
print_tree(root, "key", "left", "right" )

