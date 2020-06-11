import math

def SQRT(sklad):
	sklad.append(math.sqrt(sklad.pop()))

def GAMMA(sklad):
	sklad.append(math.gamma(sklad.pop()))

def Euler(sklad):
	sklad.append(2.718281828459045)

def PI(sklad):
	sklad.append(3.141592653589793)

def LOG(sklad):
	sklad.append(math.log(sklad.pop()) / math.log(sklad.pop())) # logaritem iz prvega na osnovi drugega

def GCD(sklad):
	sklad.append(math.gcd(sklad.pop(), sklad.pop()))

def LCA(sklad):
	a = sklad.pop()
	b = sklad.pop()
	sklad.append(a * b / math.gcd(a, b))

def kom(sklad): #povprečje
	l = sklad.pop()
	s = 0
	dol = 0
	for x in l:
		s += float(x)
		dol += 1
	s/=dol
	return s

mfs = {'+' : SQRT, '++' : GAMMA, '+++' : PI, '++++' : LOG, '+++++' : GCD, 'teta pehta' : LCA, '++++++' : abs, 'komunist' : kom, 'beži' : min, 'nebeži' : max}