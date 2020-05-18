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
			print('Vaš program ni ravno prav prijazen.')
			return 1




































	
if __name__ == '__main__':
	main()
