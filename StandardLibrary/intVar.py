try:
	from StandardLibrary.variables import Variable
	import StandardLibrary.numbery as numbery
except:
	from variables import Variable
	import numbery as number	

class INT(Variable):
	def __init__(self, value):
		if type(value) == int:
			v = value
			Variable.__init__(self, 'int', numbery.to_num(v))
			self.real_value = v

		elif type(value) == float:
			v = int(value)
			Variable.__init__(self, 'int', numbery.to_num(v))
			self.real_value = v

		elif type(value) == str:
			if ('1' in value or '2' in value or '3' in value or '4' in value or '5' in value or '6' in value or '7' in value or '8' in value or '9' in value): #je napisano z besedo
				Variable.__init__(self, 'int', numbery.to_num(value))
				self.real_value = numbery.from_num(self.value)
				
			else:
				v = value
				Variable.__init__(self, 'int', v)
				self.real_value = numbery.from_num(v)
			
		elif value.tip == 'int':
			v = value.real_value
			Variable.__init__(self, 'int', value.value)
			self.real_value = v

		elif value.tip == 'flo':
			v = int(value.real_value)
			Variable.__init__(self, 'int', value.value)
			self.real_value = v

		elif value.tip == 'ulo':
			v = int(value)
			Variable.__init__(self, 'int', numbery.to_num(v))
			self.real_value = v

		elif value.tip == 'str':
			tmp = INT(str(value))
			Variable.__init__(self, 'int', tmp.value)
			self.real_value = tmp.real_value

		else:
			try:
				v = value.real_value
			except:
				v = int(value)
			Variable.__init__(self, 'int', value.value)
			self.real_value = v



	#binary operators ###################################################
	def __add__(self, other):
		return INT(numbery.to_num(self.real_value + other.real_value))
	def __sub__(self, other):
		return INT(numbery.to_num(self.real_value - other.real_value))
	def __mul__(self, other):
		return INT(numbery.to_num(self.real_value * other.real_value))
	def __truediv__(self, other):
		return INT(numbery.to_num(round(self.real_value / other.real_value)))
	def __floordiv__(self, other):
		return INT(numbery.to_num(self.real_value // other.real_value))
	def __mod__(self, other):
		return INT(numbery.to_num(self.real_value % other.real_value))
	#unary operators
	def __str__(self):
		return self.value
	def __neg__(self):
		return INT(numbery.to_num(-numbery.from_num(self.value)))
	def __pos__(self):
		return INT(numbery.to_num(+numbery.from_num(self.value)))
	def __invert__(self):
		return INT(numbery.to_num(~numbery.from_num(self.value)))
	def __abs__(self):
		return INT(numbery.to_num(abs(self.real_value)))
	def __complex__(self):
		return complex(self.real_value)
	def __int__(self):
		return int(self.real_value)
	def __float__(self):
		return float(self.real_value)
	def __oct__(self):
		return oct(self.real_value)
	def __hex__(self):
		return hex(self.real_value)
	def __hash__(self):
		return hash(self.real_value)
	def asNumber(self):
		return str(self.real_value)
	#comparison operators
	def __lt__(self, other):
		return self.real_value < other.real_value
	def __le__(self, other):
		return self.real_value <= other.real_value
	def __eq__(self, other):
		return self.real_value == other.real_value
	def __ne__(self, other):
		return self.real_value != other.real_value
	def __ge__(self, other):
		return self.real_value >= other.real_value
	def __gt__(self, other):
		return self.real_value > other.real_value
	###################################################################
	###################################################################
