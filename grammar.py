from standardLibrary.variables import Variable
from standardLibrary.intVar import INT
from standardLibrary.narVar import NAR
from standardLibrary.uloVar import ULO
from standardLibrary.functions import *

type_to_var = {'int':INT, 'nar':NAR, 'dec':'', 'ulo':ULO, 'flo':'', 'kom':'', 'bul':'', 'črk':'', 'bes':'', 'niz':str, 'sez':list, 'mno':set, 'slo':dict}
name_to_func = {'izpiši' : printf, 'preberi' : inputf, 'preberi_celo_število' : inputint, 'preberi_ulomek':inputulo}

def check_for_kindness(program):
	prosim_naredi=0
	naredi=0
	x=1
	for line in program:
		tmp = line.split(':')[0]
		if tmp in ['prosim naredi', 'prosim definiraj', 'prosim preveri']:
			prosim_naredi += 1
		elif tmp in ['naredi', 'definiraj', 'preveri']:
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
	stack = ''
	name = ''
	value = ''
	x=0
	while x < len(s):
		stack+=s[x]
		if stack in Variable.types:
			stack=(type_to_var[stack])
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
			fn.append((stack(value), name))
			stack = ''
		x+=1
	return fn

def generate_function(s):
	f = ''
	args = ''
	target_var = ''

	x=0
	if '3' in s:
		while s[x] != '3':
			target_var += s[x]
			x+=1
		x+=1
	while s[x] != '|':
			f += s[x]
			x+=1
	x+=1
	while s[x] != 'T':
		args += s[x]
		x+=1
	args=args.split('#')

	return (target_var, name_to_func[f], args)	


class Line:
	def __init__(self, line):
		self.line = line
		self.function = []
		if line.split(':')[0] in ['definiraj', 'prosim definiraj']:
			self.tip = 'def'
		elif line.split(':')[0] in ['naredi', 'prosim naredi']:
			self.tip = 'do'
	def __str__(self):
		return str(self.line)
	def v_generate(self):
		self.function = generate_variables(self.line.split(':')[1].strip(' '))
		#print('generated'+str(self.function))
	def f_generate(self):
		self.function = generate_function(self.line.split(':')[1].strip(' '))
	def execute(self):
		return self.function