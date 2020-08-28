from standardLibrary.variables import Variable
from standardLibrary.intVar import INT
from standardLibrary.narVar import NAR
from standardLibrary.uloVar import ULO
from standardLibrary.functions import *
import math
from standardLibrary.Matematika import *

type_to_var = {'int':INT, 'nar':NAR, 'ulo':ULO, 'flo':float, 'niz':str, 'sez':list, 'mno':set, 'slo':dict}
name_to_func = {'izpiši|T' : printf, 'preberi|T' : inputf, 'preberi_celo_število|T' : inputint, 'preberi_ulomek|T':inputulo, 'izpiši|izplakni|T': print_and_flush, 'izpiši|z določenim koncem in izplakni(da/ne)T' : superprint, 'izpiši_celo_število|T' : printint}
minus_to_f = { '-' : krat, '--' : plus, '---': minus, '----': deljeno, '-----': na, '------': koren, '-------': faktorel, '--------': št_diagonal, '---------': ploščina_elipse, '----------': deljeno_z_ena}
zacetki = ['naredi', 'definiraj', 'preveri', 'potisni', 'pojej', 'izračunaj', 'komentiraj', 'poskoči na', 'poskoči za', 'uvozi', 'Prosim poslovi se od nas in umri, potem se vrni kot velika ŽOTKA, da te bomo lahko še uporabljali in imeli radi.']



def generate_variables(s):
	tip = ''
	name = ''
	value = ''
	x=0
	while not tip in Variable.types: #iskanje tipa
		tip+=s[x]
		x+=1
	tip=(type_to_var[tip])

	while s[x] != '[': # iskanje imena
		name += s[x]
		x+=1
	x+=1
	
	while s[x] != '}': # iskanje vrednosti
		value+=s[x]
		x+=1
	########################### Preverjanje, da ni številka napisana s številkami
	if tip in [INT, NAR, ULO]:
		for x in range(10):
			if x in value:
				raise Exception('Narobe napisana številka.')
	###########################
	fn = (tip(value), name)
	return fn
	
def Tip_vrstice(zacetek):
	
	if zacetek == 'definiraj':
		tip = 'def'
	elif zacetek == 'naredi':
		tip = 'do'
	elif zacetek == 'potisni':
		tip = 'push'
	elif zacetek == 'pojej':
		tip = 'eat'
	elif zacetek == 'izračunaj':
		tip = 'calc'
	elif zacetek == 'komentiraj':
		tip = 'komentar'
	elif zacetek == 'poskoči na':
		tip = 'jmp'
	elif zacetek == 'poskoči za':
		tip = 'hop' 
	elif zacetek == 'Prosim poslovi se od nas in umri, potem se vrni kot velika ŽOTKA, da te bomo lahko še uporabljali in imeli radi.':
		print('<ž++: Zbogom. Živite brez mene do mojega ponovnega klica.>')
		tip = 'stop'
	elif zacetek == 'uvozi':
		tip = 'uvozi'
	return tip

