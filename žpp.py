# -*- coding: utf-8 -*-
import sys
import StandardLibrary.numbery as numbery
import StandardLibrary.grammar as grammar
import StandardLibrary.variables as variables
from StandardLibrary.Matematika import mfs
from StandardLibrary.primerjave import primerjave
form = variables.totype
flags = sys.argv[1:]

class Vrsta:
	def __init__(self, zacetek, ukaz):
		self.ukaz = ukaz
		#print(ukaz)
		self.zacetek = zacetek
		self.tip = None
	
	def izvedi(self, program):
		#print(self.zacetek + ': ' + self.ukaz + str(program.sklad))
		if self.tip == 'def':
			program.nova_spremenljivka(grammar.generate_variables(self.ukaz))
		
		elif self.tip == 'do':
			funkcija = grammar.name_to_func[self.ukaz]
			value = funkcija(program.sklad)
			if value != None:
				program.sklad.append(value)

		elif self.tip == 'push':
			program.sklad.append(program.spremenljivke[self.ukaz])

		elif self.tip == 'eat':
			program.spremenljivke[self.ukaz] = form(type(program.spremenljivke[self.ukaz]), program.sklad.pop()) #popravi glede na tipe

		elif self.tip == 'calc':
			grammar.minus_to_f[self.ukaz](program.sklad)

		elif self.tip == 'jmp':
			program.st_vrstice = numbery.from_num(self.ukaz)
		elif self.tip == 'hop':
			program.st_vrstice += numbery.from_num(self.ukaz)
		
		elif self.tip == 'jmpp':
			if program.sklad.pop().value == 'Da':
				program.st_vrstice = numbery.from_num(self.ukaz)
		elif self.tip == 'hopp':
			if program.sklad.pop().value == 'Da':
				program.st_vrstice += numbery.from_num(self.ukaz)

		elif self.tip == 'stop':
			sys.exit(0)
		
		elif self.tip == 'uvozi':
			if self.ukaz == '<žpp - računstvo++>':
				grammar.minus_to_f.update(mfs) # dodamo matematične funkcije
		
		elif self.tip == 'primerjaj':
			primerjave[self.ukaz](program.sklad)




class Program():
	def __init__(self, vrstice):
		self.sklad = []
		self.spremenljivke = {}
		self.vrstice = vrstice
		self.st_vrstice = 0
	
	def pripravi(self, n):
		self.st_vrstice = n
	
	def preveri_prijaznost(self):
		prosim_naredi = 0
		naredi = 0
		x=3 #Števec vrstice zamaknjen za tri, za javljanje napak
		for st_vrstice in range(len(self.vrstice)):
			vrstica = self.vrstice[st_vrstice]
			if vrstica == '' and len(self.vrstice) < 2:
				del self.vrstice[st_vrstice]
				continue
			zacetek = vrstica.split(':')[0]
			konec = vrstica[len(zacetek)+2:]

			if zacetek in ['prosim '+x for x in grammar.zacetki]:
				prosim_naredi += 1
				self.vrstice[st_vrstice] = Vrsta(zacetek[7:], konec)

			elif zacetek in grammar.zacetki:
				naredi += 1
				self.vrstice[st_vrstice] = Vrsta(zacetek, konec)
			else:
				if zacetek != '':
					print('Napaka v vrstici %d.' %x)
					return 'False'
			x+=1
		
		if naredi*2 == prosim_naredi:
			return True
		else:
			return False
	
	def pridobi_tipe_vrstic(self):
		st_vr = 0
		while st_vr < len(self.vrstice):
			trenutna = self.vrstice[st_vr]
			trenutna.tip = grammar.Tip_vrstice(trenutna.zacetek)
			st_vr += 1
	
	def nova_spremenljivka(self, gen_obj):
		self.spremenljivke[gen_obj[1]] = gen_obj[0]

	def naredi(self):
		while self.st_vrstice < len(self.vrstice):
			#print(self.sklad)
			self.vrstice[self.st_vrstice].izvedi(self)
			self.st_vrstice += 1
		
		if '-i' in flags:
			cmd(self)
	
	



def cmd(program):
	while True:
		try:
			vhodna_vrstica = input('<ž++> ')
			zacetek, konec = vhodna_vrstica.split(':')

			if zacetek in ['prosim '+x for x in grammar.zacetki]:
				vrstica_za_izvedbo = Vrsta(zacetek[7:], konec)

			elif zacetek in grammar.zacetki:
				vrstica_za_izvedbo = Vrsta(zacetek, konec)

			vrstica_za_izvedbo.tip = grammar.Tip_vrstice(vrstica_za_izvedbo.zacetek)
			vrstica_za_izvedbo.izvedi(program)

		except Exception as error:
			print(error)



def main():
	name_target = flags[0]
	with open(name_target, 'r', encoding = 'utf-8') as f:
		program = Program(f.read().split('\n'))

	if (not '-forget_the_kindness' in flags) and (not '-developing_mode' in flags):
		try:
			if not program.preveri_prijaznost():
				print('Program ni ravno prav prijazen.')
				return 1
		except Exception as error:
			print('Napaka.')
			sys.exit(1)
	if '-developing_mode' in flags:		
		if not program.preveri_prijaznost():
			print('Program ni ravno prav prijazen.')
			return 1
	
	program.pripravi(0)
	program.pridobi_tipe_vrstic()
	if '-developing_mode' in flags:
		program.naredi()	
	else:
		try:
			program.naredi()
		except Exception as error:
			print('Napaka v vrstici %d.' %(program.st_vrstice+3)) #+3 je samo za zmedo
			print(error)
			return 1











	
if __name__ == '__main__':
	main()
