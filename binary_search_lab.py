# a class that inherits from the list class the following
class List:
	a,b = 0,0
	def __init__(self):
		pass

	def get_a(self):
		return self.a

	def set_a(self,a):
		self.a = a

	def get_b(self):
		return self.b

	def set_b(self,b):
		self.b = b

class BinarySearch(List):
	def __init__(self, a, b):
		self.a = a
		self.b = b


