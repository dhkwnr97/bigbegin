class TreeNode:
	def __init__(self, key, val):
		self.key=key
		self.value=val
		self._leftChild=None
		self._rightChild=None
		self.parent=None
	
	@property
	def leftChild(self):
		return self._leftChild
	@leftChild.setter
	def leftChild(self, value):
		if self._leftChild:
			self._leftChild.parent=None
		if value:
			value.parent=self
		self._leftChild=value
	@property
	def rightChild(self):
		return self._rightChild
	@rightChild.setter
	def rightChild(self, value):
		if self._rightChild:
			self._rightChild.parent=None
		if value:
			value.parent=self
		self._rightChild=value
	
	#check Method
	def isRoot(self):
		return parent is None
	def isLeaf(self):
		return (self._leftChild is None) and (self._rightChild is None)
	def isLeftChild(self):
		return (self.parent) and (self.parent._leftChild is self)
	def isRightChild(self):
		return (self.parent) and (self.parent._rightChild is self)
	def hasLeftChild(self):
		return self._leftChild is not None
	def hasRightChild(self):
		return self._rightChild is not None
	def hasBothChildren(self):
		return (self._rightChild is not None) and (self._leftChild is not None)
	def hasAnyChild(self):
		return not self.isLeaf()

class BinarySearchTree:
	def __init__(self):
		self.root=None
		self.length=0
	
	def put(self, key, val):
		if self.root:#if tree has root node, then append new node in tree
			self.__put(key, val, self.root)
		else:#if no root node, then this is a root node
			self.root=TreeNode(key, val)
	def __put(self, key, val, currentNode):#compare targetkey, new keys
		targetNode=currentNode
		while True:
			if key < targetNode.key:#enterence node`s key is less then targetnode
				if not targetNode.hasLeftChild():
					targetNode.leftChild=TreeNode(key,value)
					break
				else:
					targetNode=targetNode.leftChild#if there have child, change the target
			else:#enterence node`s key is bigger then targetnode
				if not targetNode.hasRightChild():
					targetNode.rightChild=TreeNode(key,value)
					break
				else:
					targetNode=targetNode.rightChild#if there have child, change the target
		self.length+=1#Tree size update (because append one node of leaf	
	
	searchpath=[]
	def getlessN(self, key):
		if self.root is None:
			return None
		res=self.__getlessN(key, self.root)
		if res:
			return res.value#return right darkzone: [dz_start,dz_end]
		return print("Error : There is no darkzone")
	def __getlessN(self, key, currentNode):
		targetNode=currentNode
		while True:
			if key == targetNode.key:#if same exon starting point
				searchpath=[]#find right value so, initializtion searchpath
				return targetNode, 
			elif key < targetNode.key: 
				if targetNode.hasLeftChild();
					searchpath.append([targetNode, 'L'])
					targetNode=targetNode.leftChild
				else:
					if searchpath[-1][1] == 'R':#if last path is going right
						searchpath=[]
						return targetNode.parent
					elif searchpath[-1][1] == 'L':#if last path is going left
						for eachpath in reversed(searchpath):
							if eachpath[1] == 'R':#reverse path first time meet going Right path Node
								searchpath=[]
								return eachpath[0]#return that Node 
								break
			else:
				if targetNode.hasRightChild():
					searchpath.append([targetNode.key,'R'])
					targetNode=target.rightChild
				else:
					searchpath=[]
					return targetNode