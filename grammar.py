def check_for_kindness(program):
	prosim_naredi=0
	naredi=0
	x=1
	for line in program:
		tmp = line.split(':')[0]
		if tmp in ['prosim naredi', 'prosim definiraj', 'prosim preveri']:
			prosim_naredi += 1
		elif tmp in ['naredi', 'definiraj', 'preveri']:
			naredi += 1
		else:
			if tmp != '':
				print('Napaka v vrstici %d.' %x)
				return 1
		x+=1
	
	if naredi*2 == prosim_naredi:
	 	return True
	else:
	 	return False

class Line:
	def __init__(self, line):
		self.line = line
	def __str__(self):
		return id(self.line)
