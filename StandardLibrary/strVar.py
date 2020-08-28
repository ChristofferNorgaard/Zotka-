from standardLibrary.variables import Variable
import standardLibrary.numbery as numbery

class STR(Variable):
	def __init__(self, value):
		Variable.__init__(self, 'str', str(value))



	#binary operators ###################################################
	def __add__(self, other):
		return STR(self.value + other.value)
	def __sub__(self, other):
		return STR(self.value[int(other)])
	#unary operators
	def __str__(self):
		return self.value
	def __invert__(self):
		return INT(numbery.to_num(~numbery.from_num(self.value)))
	def __abs__(self):
		return len(self.value)
	def __hash__(self):
		return hash(self.value)
	#comparison operators
	def __lt__(self, other):
		return self.value < other.value
	def __le__(self, other):
		return self.value <= other.value
	def __eq__(self, other):
		return self.value == other.value
	def __ne__(self, other):
		return self.value != other.value
	def __ge__(self, other):
		return self.value >= other.value
	def __gt__(self, other):
		return self.value > other.value
	###################################################################
	###################################################################
