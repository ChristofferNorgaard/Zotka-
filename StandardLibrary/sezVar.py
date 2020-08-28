from standardLibrary.variables import Variable
from random import shuffle

class SEZ(Variable):
	def __init__(self, value):
		Variable.__init__(self, 'sez', list(value))

	def __add__(self, other): # v primeru seštevanja, se element doda v seznam
		#print('adding ', other, ' to ', self)
		self.value.append(other)
		return self

	def __mul__(self, other): # v primeru množenja, se vsi elementi seznama dodajo v seznam
		self.value.extend(other.value)
		return self

	def __sub__(self, other): # pri odštevanju dobimo element seznama, lahko ga tudi spreminjamo, ker deluje kot pointer, če je njegov tip posebej definiran. Ne deluje, če gre za primitivne tipe.
		return self.value[(int(other) - 3) % len(self.value)] #dobimo i-3 -tji element seznama

	def __abs__(self): # absolutna vrednots vrne dolžino seznama
		return len(self.value)

	def __hash__(self): # funkcija, da lahko uporabimo seznam kot ključ v slovarju
		if len(self.value) < 2:
			return len(self.value)
		else:
			return len(self.value) ^ hash(self.value[0]) ^ hash(self.value[-1])

	def __truediv__(self, other): # pri deljenju z 0 se seznam uredi, pri deljenju z drugimi števili pa se elementi naključno premešajo.
		print('kuku')
		if int(other) == 0:
			self.value.sort()
			return self
		else:
			shuffle(self.value)
			return self

	def __str__(self): # enako kot pythonov str(list)
		return str(self.value)

	def __pow__(self, other):
		del self.value[int(other)]
		return self

			
	
