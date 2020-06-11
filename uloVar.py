from standardLibrary.variables import Variable
from standardLibrary.intVar import INT
import standardLibrary.numbery as numbery
from math import gcd

def lcm(a, b):
	return a*b/gcd(a, b)

class ULO(Variable):
	def __init__(self, value):
		if '$' in value:
			up, down = value.split('$')
			Variable.__init__(self, 'ulo', (up, down))
			try:
				self.real_up = numbery.from_num(up)
				self.real_down = numbery.from_num(down)
				if self.real_down < 0:
					self.real_down *= -1
					self.real_up *= -1
				tmp=gcd(self.real_down, self.real_up)
				self.real_up /= tmp
				self.real_down /= tmp
				self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))
				del tmp
			except Exception as error:
				print(error)
				raise Exception('Napaka pri zapisu števila. Omejitev je 999 999 999 999. Pri večjih številih je dogajanje nepredvidljivo.')
		else:
			up, down = from_float(float(value)).value
			Variable.__init__(self, 'ulo', (up, down))
			try:
				self.real_up = numbery.from_num(up)
				self.real_down = numbery.from_num(down)
				if self.real_down < 0:
					self.real_down *= -1
					self.real_up *= -1
				tmp=gcd(self.real_down, self.real_up)
				self.real_up /= tmp
				self.real_down /= tmp
				self.value = (numbery.to_num(self.real_up), numbery.to_num(self.real_down))
				del tmp
			except Exception as error:
				print(error)
				raise Exception('Napaka pri zapisu števila. Omejitev je 999 999 999 999. Pri večjih številih je dogajanje nepredvidljivo.')

	#binary operators
	def __add__(self, other):
		tmp = gcd(self.real_down, other.real_down)
		return ULO(numbery.to_num(self.real_up*tmp + other.real_up*tmp), lcm(self.real_down, other.real_down))
	def __sub__(self, other):
		tmp = gcd(self.real_down, other.real_down)
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
			return ULO(numbery.to_num(v)+'$ena') + ULO('ena$ena')/from_sklad(u)
		else:
			return ULO(numbery.to_num(v)+'$ena')