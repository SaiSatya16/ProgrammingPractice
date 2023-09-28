# Python program to evaluate value of a postfix
# expression with integers containing multiple digits


class evalpostfix:
	def __init__(self):
		self.stack = []
		self.top = -1

	def pop(self):
		if self.top == -1:
			return
		else:
			self.top -= 1
			return self.stack.pop()

	def push(self, i):
		self.top += 1
		self.stack.append(i)

	def centralfunc(self, ab):
		for i in ab:

			# If the component of the list is an integer
			try:
				self.push(int(i))
			
			# If the component of the list is not an integer,
			# it must be an operator. Using ValueError, we can
			# evaluate components of the list other than type int
			except ValueError:
				val1 = self.pop()
				val2 = self.pop()
				if i == '/':
					self.push(val2 / val1)
				else:
					
					# Switch statement to perform operation
					switcher = {'+': val2 + val1, '-': val2 -
								val1, '*': val2 * val1, '^': val2**val1}
					self.push(switcher.get(i))
		return int(self.pop())



# Driver code
if __name__ == '__main__':
	str = '100 200 + 2 / 5 * 7 +'
	
	# Splitting the given string to obtain
	# integers and operators into a list
	strconv = str.split(' ')
	obj = evalpostfix()
	print(obj.centralfunc(strconv))

# This code is contributed by Amarnath Reddy

      