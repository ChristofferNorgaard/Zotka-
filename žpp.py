# -*- coding: utf-8 -*-
import sys
import standardLibrary.numbery as numbery
import standardLibrary.grammar as grammar
import standardLibrary.variables as variables
form = variables.totype
flags = sys.argv[1:]


def naredi(program):
	sklad=[]
	vars={}
	lines=[]
	for line in range(len(program)):
			lines.append(grammar.Line(program[line]))
			tmp = lines[-1]

			if tmp.tip == 'def':
				tmp.v_generate()
				if len(tmp.execute()) > 0:
					vars[tmp.execute()[0][1]] = tmp.execute()[0][0]
			
			elif tmp.tip == 'do':
				tmp.f_generate()
				function = tmp.execute()
				value = function(sklad)
				if value != None:
					sklad.append(value)

			elif tmp.tip == 'push':
				sklad.append(vars[tmp.push()])

			elif tmp.tip == 'eat':
				vars[tmp.eat()] = form(type(vars[tmp.eat()]), sklad.pop()) #popravi glede na tipe

			elif tmp.tip == 'calc':
				tmp.calculate()(sklad)




def main():
	name_target = flags[0]
	with open(name_target, 'r', encoding = 'utf-8') as f:
		program = f.read().split('\n')

	if not '-forget_the_kindness' in flags:
		if not grammar.check_for_kindness(program):
			print('Program ni ravno prav prijazen.')
			return 1
	
	
	if '-developing_mode' in flags:
		naredi(program)		
	else:
		try:
			naredi(program)
		except Exception as error:
			print('Napaka v vrstici %d.' %line)
			print(error)
			return 1

































	
if __name__ == '__main__':
	main()
