try:
    import StandardLibrary.numbery as numbery
except ModuleNotFoundError:
    import numbery
    
class Variable:
	types = {'celo število', 'naravno število', 'ulo', 'flo', 'bul', 'niz', 'sez', 'slo', 'str'}
	def __init__(self, tip, value):
		if tip in Variable.types:
			self.tipe = tip
			self.value = value
		else:
			raise Exception(tip + ' je neprepoznana vrsta spremenljivke.')

def totype(tip, value):
	return tip(value)
