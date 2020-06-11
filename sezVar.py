from standardLibrary.variables import Variable
import standardLibrary.numbery as numbery
from random import shuffle

class SEZ(Variable):
	def __init__(self, value):
		Variable.__init__(self, 'sez', list(value))

	def __add__(self, other):
		#print('adding ', other, ' to ', self)
		self.value.append(other)
		return self

	def __mul__(self, other):
		self.value.extend(other.value)
		return self

	def __sub__(self, other):
		return self.value[(int(other) - 3) % len(self.value)] #dobimo i-3 -tji element seznama

	def __abs__(self):
		return len(self.value)

	def __hash__(self):
		if len(self.value) < 2:
			return len(self.value)
		else:
			return len(self.value) ^ hash(self.value[0]) ^ hash(self.value[-1])

	def __div__(self, other):
		if int(other) == 1:
			self.value.sort()
			return self
		else:
			shuffle(self.value)
			return self

	def __str__(self):
		return str(self.value)


			
	
