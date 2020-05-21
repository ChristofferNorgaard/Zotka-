import standardLibrary.numbery as numbery

class Variable:
	types = {'int', 'nar', 'dec', 'ulo', 'flo', 'kom', 'bul', 'črk', 'bes', 'niz', 'sez', 'mno', 'slo'}
	def __init__(self, tip, value):
		if tip in Variable.types:
			self.tipe = tip
			self.value = value
		else:
			raise Exception('Neprepoznana vrsta spremenljivke.')

def totype(tip, value):
	return tip(value)
