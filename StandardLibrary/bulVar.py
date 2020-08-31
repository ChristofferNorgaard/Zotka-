try:
	from StandardLibrary.variables import Variable
except:
	from variables import Variable

class BUL(Variable):
	def __init__(self, value):
		Variable.__init__(self, 'bul', value)
		if type(value) == BUL:
			self.value = value.value
			self.bl = value.bl
		elif value in ['Da', 'Ne']:
			self.value = value
			self.bl = {'Da':True, 'Ne':False}[value]
		elif value in [True, False]:
			self.bl = value
			self.value = {True:'Da', False:'Ne'}[value]
		
		else:
			raise  Exception(str(value) + ' ni prava vrednost za bul.')



	#binary operators ###################################################
	def __add__(self, other):
		return BUL(self.bl or other.bl)
	def __sub__(self, other):
		#print('here', [BUL(self.bl ^ other.bl)])
		return BUL(self.bl ^ other.bl)
	def __mul__(self, other):
		return BUL(self.bl and other.bl)
	#unary operators
	def __str__(self):
		return str(self.value)
	def __int__(self):
		return int(self.bl)
	def __float__(self):
		return float(self.bl)
	def __hash__(self):
		return hash(self.bl)
	def asNumber(self):
		return str(int(self))
	#comparison operators
	def __lt__(self, other):
		return BUL(self.bl < other.bl)
	def __le__(self, other):
		return BUL(self.bl <= other.bl)
	def __eq__(self, other):
		#print([self, other])
		return BUL(self.bl == other.bl)
	def __ne__(self, other):
		return BUL(self.bl != other.bl)
	def __ge__(self, other):
		return BUL(self.bl >= other.bl)
	def __gt__(self, other):
		return BUL(self.bl > other.bl)
	###################################################################
	###################################################################
