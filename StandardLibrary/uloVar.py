try:
	from standardLibrary.variables import Variable
	import standardLibrary.numbery as numbery

except Exception as e:
	#print(e)
	from variables import Variable
	import numbery as numbery

from math import gcd

def lcm(a, b):
	return int(a*b/gcd(int(a), int(b)))

class ULO(Variable):
	def __init__(self, value, *v):
		Variable.__init__(self, 'ulo', (1, 1))
		if len(v) == 1:
			self.value = (value, v)
			self.real_up = numbery.from_num(value)
			self.real_down = numbery.from_num(v[0])

		elif type(value) == str:
			if '$' in value:
				up, down = value.split('$')
				self.value = (up, down)
				
				try:
					self.real_up = numbery.from_num(up)
					self.real_down = numbery.from_num(down)

					tmp=gcd(int(self.real_down), int(self.real_up))
					self.real_up /= tmp
					self.real_down /= tmp
					self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))
				except Exception as error:
					print(error)
					raise Exception('Napaka pri zapisu števila.')
			else:
				up, down = from_float(float(value)).value
			self.value = (up, down)

		elif type(value) == float:
			self.value = from_float(value).value
			up, down = self.value
			self.real_up, self.real_down = numbery.from_num(up), numbery.from_num(down)

		elif type(value) == int:
			self.value = from_float(float(value)).value
			up, down = self.value
			self.real_up, self.real_down = numbery.from_num(up), numbery.from_num(down)

		elif value.tip == 'str':
			tmp = ULO(str(value))
			self.real_up = tmp.real_up
			self.real_down = tmp.real_down
			self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))

		elif value.tip == 'int':
			tmp = ULO(int(value))
			self.real_up = tmp.real_up
			self.real_down = tmp.real_down
			self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))

		elif value.tip == 'nar':
			tmp = ULO(int(value))
			self.real_up = tmp.real_up
			self.real_down = tmp.real_down
			self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))

		elif value.tip == 'ulo':
			self = value.copy()
			
		self.real_up = int(self.real_up)
		self.real_down = int(self.real_down)
		if type(self.value[1]) == tuple:
			print(type(value)) 
		print(self.value, self.real_up, self.real_down)



	#binary operators
	def __add__(self, other):
		tmp = gcd(int(self.real_down), int(other.real_down))
		return ULO(numbery.to_num(self.real_up*tmp + other.real_up*tmp), lcm(self.real_down, other.real_down))
	def __sub__(self, other):
		tmp = gcd(int(self.real_down), int(other.real_down))
		return ULO(numbery.to_num(self.real_up*tmp - other.real_up*tmp), lcm(self.real_down, other.real_down))
	def __mul__(self, other):
		return ULO(numbery.to_num(self.real_up * other.real_up), numbery.to_num(self.real_down * other.real_down))
	def __truediv__(self, other):
		return ULO(numbery.to_num(self.real_up * other.real_down), numbery.to_num(self.real_down * other.real_up))
	def __pow__(self, other):
		return ULO(numbery.to_num(self.real_up ** other), numbery.to_num(self.real_down ** other))
	#unary operators
	def __str__(self):
		return self.value[0]+'$'+self.value[1]
	def __neg__(self):
		return ULO(numbery.to_num(-numbery.from_num(self.real_up)), self.real_down)
	def __pos__(self):
		return ULO(numbery.to_num(+numbery.from_num(self.real_up)), self.real_down)
	def __abs__(self):
		return ULO(numbery.to_num(abs(self.real_up)), self.real_down)
	def __complex__(self):
		return complex(float(self.real_up/self.real_down))
	def __int__(self):
		return int(self.real_up/self.real_down)
	def __float__(self):
		return float(self.real_up/self.real_down)
	def __oct__(self):
		return oct(self.real_value)
	def __hex__(self):
		return hex(self.real_value)
	def __hash__(self):
		return hash(self.value)
	def asNumber(self):
		return self.value[0]+', '+self.value[1]
	#comparison operators
	def __lt__(self, other):
		return float(self) < float(other)
	def __le__(self, other):
		return float(self) <= float(other)
	def __eq__(self, other):
		return float(self) == float(other)
	def __ne__(self, other):
		return float(self) != float(other)
	def __ge__(self, other):
		return float(self) >= float(other)
	def __gt__(self, other):
		return float(self) > float(other)
	###################################################################
	###################################################################
def from_float(value):
		val=float(value)
		v = int(val)
		o = val - v
		if o > 0.0001:
			u = 1/o
			return ULO(numbery.to_num(v)+'$ena') + ULO('ena$ena')/from_float(u)
		else:
			return ULO(numbery.to_num(v)+'$ena')