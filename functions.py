from standardLibrary.numbery import from_num, to_num
from math import gamma
from math import pi
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
	sklad.append(float(sklad.pop())*float(sklad.pop()))

def plus(sklad):
	sklad.append(float(sklad.pop())+float(sklad.pop()))

def minus(sklad):
	sklad.append(float(sklad.pop())-float(sklad.pop()))

def deljeno(sklad):
	sklad.append(float(sklad.pop())/float(sklad.pop()))

def na(sklad):
	sklad.append(float(sklad.pop())**float(sklad.pop()))

def koren(sklad):
	sklad.append(float(sklad.pop())**(1/float(sklad.pop())))

def faktorel(sklad):
	sklad.append(gamma(float(sklad.pop()) + 1))

def št_diagonal(sklad):
	n=int(sklad.pop())+int(sklad.pop())
	sklad.append(n*(n-3)/2)

def ploščina_elipse(sklad):
	sklad.append(float(sklad.pop())*float(sklad.pop())*pi)

def deljeno_z_ena(sklad):
	pass