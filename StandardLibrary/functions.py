try:
	from StandardLibrary.numbery import from_num, to_num
	from StandardLibrary.sezVar import SEZ
	from StandardLibrary.sloVar import SLO
except:
	from numbery import from_num, to_num
	from sezVar import SEZ
	from sloVar import SLO

from math import gamma, pi

'''
pojej - vzame vrednost iz sklad
potisni - doda vrednost na sklad
izračunaj - izračuna zadnji dve zadevi na skladu in to doda na sklad

operacije:
	- krat
	-- plus
	--- minus
	---- deljeno
	----- na
	------ koren
	------- faktorel
	-------- število diagonal pravilnega večkotnika seštevka teh dveh števil
	--------- ploščina elipse s tema polmeroma
	---------- deljeno z ena

definiraj - definira novo spremenljivko (prosim definiraj: intime spremenljivke[petsto-petdeset})
izpisovanje:
	prosim potisni: besedilo
	prosim naredi: izpiši|T


'''
def printf(sklad):
	print(sklad.pop())

def printint(sklad):
	print(int(sklad.pop()))

		
def inputf(sklad):
	r = input()
	sklad.append(r)

def inputint(sklad):
	sklad.append(to_num(input()))

def inputulo(sklad):
	sklad.append('$'.join([to_num(x) for x in input().split('/')]))

def print_and_flush(sklad):
	print(sklad.pop(), flush=True)

def superprint(sklad):
	print(sklad.pop(), end=sklad.pop(), flush=bool(sklad.pop()))

def krat(sklad):
	a = sklad.pop()
	b = sklad.pop()
	sklad.append(a*b)

def plus(sklad):
	b = sklad.pop()
	a = sklad.pop()
	
	if type(a) == type(b) or type(a) == SEZ or type(a) == SLO:
		sklad.append(a+b)
	else:
		sklad.append(float(a)+float(b))
	#print(sklad)

def minus(sklad):
	b = sklad.pop()
	a = sklad.pop()
	
	if type(a) == type(b) or type(a) == SEZ or type(a) == SLO:
		r = a-b
		sklad.append(r)
	else:
		print(type(a))
		print(type(b))
		sklad.append(float(a)-float(b))


def deljeno(sklad):
	a = sklad.pop()
	b = sklad.pop()
	if type(a) == type(b) or type(a) == SEZ:
		print('kuku')
		sklad.append(a/b)
	else:
		sklad.append(float(a)/float(b))
		
def na(sklad):
	a = sklad.pop()
	b = sklad.pop()
	if type(a) == type(b):
		sklad.append(a**b)
	else:
		sklad.append(float(a)**float(b))

def koren(sklad):
	a = sklad.pop()
	b = sklad.pop()
	if type(a) == type(b):
		sklad.append(a**float(1/b))
	else:
		sklad.append(float(a)**float(1/float(b)))

def faktorel(sklad):
	a = sklad.pop()
	sklad.append(type(a)(gamma(float(a) + 1)))

def št_diagonal(sklad):
	a = sklad.pop()
	b = sklad.pop()
	if type(a) == type(b):
		n = a + b
		sklad.append(n*(n-type(a)(3))/type(a)(2))
	else:
		n=int(a)+int(b)
		sklad.append(type(a)(n*(n-3)/2))
		


def ploščina_elipse(sklad):
	a = sklad.pop()
	b = sklad.pop()
	sklad.append(a*b*pi)

def deljeno_z_ena(sklad):
	pass