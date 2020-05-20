from standardLibrary.numbery import from_num, to_num
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
def printf(text):
	try:
		print(''.join(text))
	except:
		print(text)
		
def inputf(question):
	try:
		r = input(''.join(question))
		return r
	except:
		return input(question)

def inputint(question):
	return to_num(inputf(question))

def inputulo(question):
	return '$'.join([to_num(x) for x in inputf(question).split('/')])