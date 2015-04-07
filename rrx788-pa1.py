import Queue

def twoToTheN(n):
	"""Computes 2^n in log(n) time"""
	if n==0:
		return 1
	elif n==1:
		return 2
	else:
		x = twoToTheN(n/2)
		if n%2==0:
			return x*x
		else:
			return 2*x*x

def mean(L):
	"""Computes the average of a list L"""
	x = sum(L)
	y = len(L)
	return x/float(y)

def median(L):
	"""Computes the median of a list L"""
	L.sort()
	x = len(L)
	if x%2==1:
		return L[x/2]
	else:
		return (L[x/2 - 1] + L[x/2])/float(2)

class myQueue:
	def __init__(self):
		self.i = []

	def put(self,item):
		self.i.append(item)

	def get(self):
		return self.i.pop(0)

	def empty(self):
		if not self.i:
			return True
		else:
			return False

def bfs(tree, elem):
	"""Determines if elem exist in tree using bfs search"""

	q = myQueue()
	
	q.put(tree) #start the iterative process by placing root in our Queue

	while not q.empty():

		x = q.get()

		if type(x) is not list:

			print x

			if x==elem:
				return True

	 	else:
			for i in x:
				q.put(i)

	return False

def dfs(tree, elem):
	"""Determines if elem exist tree using dfs search"""
	
	tree = recurReverse(tree) # reverse order of tree for use as stack
	
	while tree:

		x = tree.pop()

		if type(x) is not list:
			
			print x

			if x==elem:
				return True

		else:
			
			if x:
				y = x.pop()	
				tree.append(x)
				tree.append(y)

	return False	

def recurReverse(L):
	"""Reverse list and any items that are list recursively"""
	
	if type(L) is list:
		L3 = L[:]
		L2 = []
		while L3:
			L2.append(recurReverse(L3.pop()))

		return L2
	else:
		return L


class TTTBoard:
	def __init__(self):
		"""intialize the TTTBoard class """

		self.board = ["*"]*9

	def __str__(self):
		"""function to print class using standard output"""

		str2 = "\n"

		for i, v in enumerate(self.board):

			if (i+1)%3==0:
				str2 = str2 + " " + v +'\n'
			else:
				str2 = str2 + " " + v

		return str2

	def makeMove(self, player, pos):
		"""set a player x or o in specified position"""

		if pos < 0 or pos > 8:
			return False

		elif self.board[pos] is not "*":
			return False

		else:
			self.board[pos] = player
			return True

	def hasWon(self, player):
		"""checks if the specified player has won the game"""

		for i in range(0,3):
			if self.board[0+i*3]==player and self.board[1+i*3]==player and self.board[2+i*3]==player:
				return True
			if self.board[0+i]==player and self.board[3+i]==player and self.board[6+i]==player:
				return True
			if self.board[0]==player and self.board[4]==player and self.board[8]==player:
				return True
			if self.board[2]==player and self.board[4]==player and self.board[6]==player:
				return True

		return False

	def gameOver(self):
		"""Returns true if someone has won and false otherwise"""

		if self.hasWon("X") or self.hasWon("O"):
			return True
		elif "*" in self.Board:
			return False
		else:
			return True

	def clear(self):
		"""Clears the board"""

		self.board = ["*"]*9