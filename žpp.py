# -*- coding: utf-8 -*-
import sys
import standardLibrary.numbery as numbery
import standardLibrary.grammar as grammar
import standardLibrary.variables as variables
flags = sys.argv[1:]


def main():
	name_target = flags[0]
	with open(name_target, 'r', encoding = 'utf-8') as f:
		program = f.read().split('\n')

	if not '-forget_the_kindness' in flags:
		if not grammar.check_for_kindness(program):
			print('Program ni ravno prav prijazen.')
			return 1
	
	vars={}
	lines=[]
	for line in program:
		lines.append(grammar.Line(line))
		tmp = lines[-1]
		if tmp.tip == 'def':
			tmp.v_generate()
			if len(tmp.execute()) > 0:
				vars[tmp.execute()[0][1]] = tmp.execute()[0][0]
		
		elif tmp.tip == 'do':
			tmp.f_generate()
			target, function, arguments = tmp.execute()
			if target != '':
				if target in vars.keys():
					vars[target] = type(vars[target])(function(arguments))
			else:
				function([str(vars[x]) for x in arguments])

	



































	
if __name__ == '__main__':
	main()
