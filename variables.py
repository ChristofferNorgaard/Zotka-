import standardLibrary.numbery

class Variable:
	types = {'int', 'nar', 'dec', 'ulo', 'flo', 'kom', 'bul', 'črk', 'bes', 'niz', 'sez', 'mno', 'slo'}
	def __init__(self, tip, value):
		if tip in Variable.types:
			self.tipe = tip
			self.value = value
		else:
			raise TypeError

