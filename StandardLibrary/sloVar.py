try:
	from StandardLibrary.variables import Variable
	from StandardLibrary.sezVar import SEZ
except:
	from variables import Variable
	from sezVar import SEZ
from random import shuffle

class SLO(Variable):
	def __init__(self, value):
		Variable.__init__(self, 'sez', dict())

	def __add__(self, keyval): # v primeru seštevanja, se doda v slovar
		self.value[keyval.value[0]] = keyval.value[1]
		return self

	def __mul__(self, other): # v primeru množenja, slovar razširi za drug slovar
		self.value.update(other.value)
		return self

	def __sub__(self, other): # pri odštevanju dobimo element slovara, lahko ga tudi spreminjamo, ker deluje kot pointer, če je njegov tip posebej definiran. Ne deluje, če gre za primitivne tipe.
		return self.value[other] 

	def __abs__(self): # absolutna vrednost vrne dolžino slovarja
		return len(self.value)

	def __hash__(self): # funkcija, da lahko uporabimo slovar kot ključ v slovarju
		if len(self.value) < 2:
			return len(self.value)
		else:
			return len(self.value) ^ hash(list(self.value)[0]) ^ hash(list(self.value)[-1])

	def __str__(self): # enako kot pythonov str(dict)
		return str(self.value)

	def __truediv__(self, other):
		del self.value[other]
		return self

	def __pow__(self, other):
		if int(other) == 0:
			r = SEZ()
			r.value = list(self.value.keys())
			return r
		else:
			r = SEZ()
			r.value = list(self.value.values())
			return r
