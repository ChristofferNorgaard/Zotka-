from standardLibrary.variables import Variable
from standardLibrary.intVar import INT
from standardLibrary.narVar import NAR
from standardLibrary.uloVar import ULO
from standardLibrary.functions import *

type_to_var = {'int':INT, 'nar':NAR, 'dec':'', 'ulo':ULO, 'flo':'', 'kom':'', 'bul':'', 'črk':'', 'bes':'', 'niz':str, 'sez':list, 'mno':set, 'slo':dict}
name_to_func = {'izpiši|T' : printf, 'preberi|T' : inputf, 'preberi_celo_število|T' : inputint, 'preberi_ulomek|T':inputulo, 'izpiši|izplakni|T': print_and_flush, 'izpiši|z določenim koncem in izplakni(da/ne)T' : superprint, 'izpiši_celo_število|T' : printint}
minus_to_f = { '-' : krat, '--' : plus, '---': minus, '----': deljeno, '-----': na, '------': koren, '-------': faktorel, '--------': št_diagonal, '---------': ploščina_elipse, '----------': deljeno_z_ena}

def check_for_kindness(program):
	zacetki = ['naredi', 'definiraj', 'preveri', 'potisni', 'pojej', 'izračunaj', 'komentiraj']
	prosim_naredi=0
	naredi=0
	x=1
	for line in program:
		tmp = line.split(':')[0]
		if tmp in ['prosim '+x for x in zacetki]:
			prosim_naredi += 1
		elif tmp in zacetki:
			naredi += 1
		else:
			if tmp != '':
				print('Napaka v vrstici %d.' %x)
				return 1
		x+=1
	
	if naredi*2 == prosim_naredi:
	 	return True
	else:
	 	return False

def generate_variables(s):
	fn = []
	tip = ''
	name = ''
	value = ''
	x=0
	while x < len(s):
		tip+=s[x]
		if tip in Variable.types:
			tip=(type_to_var[tip])
			name=''
			x+=1
			while s[x] != '[':
				name += s[x]
				x+=1
			x+=1
			value=''
			while s[x] != '}':
				value+=s[x]
				x+=1
			fn.append((tip(value), name))
			tip = ''
		x+=1
	return fn
	


class Line:
	def __init__(self, line):
		self.line = line
		self.function = []
		levo = line.split(':')[0]
		self.desno = line[len(levo)+2:] 
		
		if levo in ['definiraj', 'prosim definiraj']:
			self.tip = 'def'
		elif levo in ['naredi', 'prosim naredi']:
			self.tip = 'do'
		elif levo in ['potisni', 'prosim potisni']:
			self.tip = 'push'
		elif levo in ['pojej', 'prosim pojej']:
			self.tip = 'eat'
		elif levo in ['izračunaj', 'prosim izračunaj']:
			self.tip = 'calc'
		elif levo in ['komentiraj', 'prosim komentiraj']:
			self.tip = 'komentar'

	def __str__(self):
		return str(self.line)
	
	def v_generate(self):
		self.function = generate_variables(self.desno)
		#print('generated'+str(self.function))
	def f_generate(self):
		self.function = name_to_func[self.desno]
	def push(self):
		return self.desno
	def eat(self):
		return self.desno
	def execute(self):
		return self.function
	def calculate(self):
		return minus_to_f[self.desno]