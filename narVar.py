from variables import Variable
from intVar import INT
import numbery

class INT(NAR):
	def __init__(self, value):
		if value < 3:
			print('nar je lahko le naravno število večje od 2.')
			raise ValueError
		Variable.__init__(self, 'nar', value)
		try:
			self.real_value = numbery.from_num(value)
		except Exception as error:
			print('Napaka pri zapisu števila. Omejitev je 999 999 999 999. Pri večjih številih je dogajanje nepredvidljivo.')
			print(error)
			raise NumberError

	#binary operators ###################################################################
	def __add__(self, other):
		return NAR(numbery.to_num(self.real_value + other.real_value))
	def __sub__(self, other):
		return NAR(numbery.to_num(self.real_value - other.real_value))
	def __mul__(self, other):
		return NAR(numbery.to_num(self.real_value * other.real_value))
	def __truediv__(self, other):
		return NAR(numbery.to_num(self.real_value // other.real_value))
	def __floordiv__(self, other):
		return NAR(numbery.to_num(round(self.real_value / other.real_value)))
	def __mod__(self, other):
		return NAR(numbery.to_num(self.real_value % other.real_value))
	def __pow__(self, other):
		return NAR(numbery.to_num(self.real_value ** other.real_value))
	#unary operators ###################################################################
	def __str__(self):
		return self.value
	def __neg__(self):
		return NAR(numbery.to_num(-numbery.from_num(self.value)))
	def __pos__(self):
		return NAR(numbery.to_num(+numbery.from_num(self.value)))
	def __invert__(self):
		return NAR(numbery.to_num(~numbery.from_num(self.value)))
	def __abs__(self):
		return NAR(numbery.to_num(abs(self.real_value)))
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
	#comparison operators ###################################################################
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