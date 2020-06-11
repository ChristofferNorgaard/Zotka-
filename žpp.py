# -*- coding: utf-8 -*-
import sys
import standardLibrary.numbery as numbery
import standardLibrary.grammar as grammar
import standardLibrary.variables as variables
form = variables.totype
flags = sys.argv[1:]

def izvedi_vrstico(sklad, vars, line, tmp):
	#print(vars)
	#print(sklad)
	#print()
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

	elif tmp.tip == 'jmp':
		line[0] = numbery.from_num(tmp.desno)
	elif tmp.tip == 'hop':
		line[0] += numbery.from_num(tmp.desno)

	elif tmp.tip == 'stop':
		sys.exit(0)

def naredi(program, ln):
	sklad=[]
	vars={}
	lines=[]
	line = [0]
	while line[0] < len(program):
		#print(sklad)
		ln[0] = line[0]
		lines.append(grammar.Line(program[line[0]]))
		tmp = lines[-1]
		izvedi_vrstico(sklad, vars, line, tmp)
		#print('\b'*3 + str(line[0]), end='')
		line[0] += 1
	if '-i' in flags:
		cmd(program, sklad, vars, line, lines, ln)

def cmd(program, sklad, vars, line, lines, ln):
	while True:
		try:
			ln[0] = line[0]
			lines.append(grammar.Line(input('<ž++> ')))
			tmp = lines[-1]
			izvedi_vrstico(sklad, vars, line, tmp)
			line[0] += 1
		except Exception as error:
			print(error)

def main():
	name_target = flags[0]
	with open(name_target, 'r', encoding = 'utf-8') as f:
		program = f.read().split('\n')

	if not '-forget_the_kindness' in flags:
		if not grammar.check_for_kindness(program):
			print('Program ni ravno prav prijazen.')
			return 1
	
	ln=[0]
	if '-developing_mode' in flags:
		naredi(program, ln)		
	else:
		try:
			naredi(program, ln)
		except Exception as error:
			print('Napaka v vrstici %d.' %(ln[0]+3)) #+3 je samo za zmedo
			print(error)
			return 1

































	
if __name__ == '__main__':
	main()
