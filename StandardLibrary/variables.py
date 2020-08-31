try:
    import StandardLibrary.numbery as numbery
except ModuleNotFoundError:
    import numbery
    
class Variable:
	types = {'int', 'nar', 'dec', 'ulo', 'flo', 'kom', 'bul', 'črk', 'bes', 'niz', 'sez', 'mno', 'slo', 'str'}
	def __init__(self, tip, value):
		if tip in Variable.types:
			self.tipe = tip
			self.value = value
		else:
			raise Exception(tip + ' je neprepoznana vrsta spremenljivke.')

def totype(tip, value):
	return tip(value)
