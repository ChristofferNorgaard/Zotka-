import math

mfs = {'+' : SQRT, '++' : GAMMA, '+++' : PI, '++++' : LOG, 'teta Pehta' : GCD}

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