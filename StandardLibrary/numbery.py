import math

def razporedi_po_tri(x):
	s = str(x)[::-1] #od zadaj
	r = ['']*math.ceil(len(s)/3) #pripravim prostor za števke 
	for x in range(len(s)):
		r[x//3] += s[x]

	for x in range(len(r)):
		r[x] = int(r[x][::-1])

	return r[::-1]


do10 = lambda x: ['', 'ena', 'dva', 'tri', 'štiri', 'pet', 'šest', 'sedem', 'osem', 'devet'][x]
po10 = lambda x: ['', 'najst', 'dvajset', 'trideset', 'štirideset', 'petdeset', 'šestdeset', 'sedemdeset', 'osemdeset', 'devetdeset'][x]
po100 = lambda x: ['', 'sto', 'dvesto', 'tristo', 'štiristo', 'petsto', 'šeststo', 'sedemsto', 'osemsto', 'devetsto'][x]

def do100(x):
	if x < 10:
		return do10(x)
	if x == 10:
		return 'deset'
	if x == 11:
		return 'enajst'
	if x < 20:
		return do10(x%10) + po10(x//10)
	if x%10 == 0:
		return po10(x//10)
	return do10(x%10) + 'in' + po10(x//10)

def do1000(x):
	r = po100(x//100) + '-' + do100(x%100)
	if len(r) > 0 and '-' == r[0]:
		r = r[1:]
	if len(r) > 0 and '-' == r[-1]:
		r = r[:-1]
	return r

def do1e6(x):
	if x < 1000:
		return do1000(x)
	if x == 1000:
		return 'tisoč'
	if x < 2000:
		return 'tisoč-' + do1000(x % 1000)

	if x % 1000 == 0:
		return do1000(x//1000) + '-tisoč'
	return do1000(x//1000) + '-tisoč-' + do1000(x%1000)

def sklanjaj(s, nacin):
	if s.endswith('ena'):
		if nacin == 0: #primer: en milijon
			tmp = ''
		else: #primer: ena milijarda
			tmp = 'a' 
		return (s[:-1] + tmp, 'ena')

	if s.endswith('dva'):
		if nacin == 0: #primer: dva milijona
			tmp = 'a'
		else: #primer: dve milijardi
			tmp = 'e' 
		return (s[:-1] + tmp, 'dva')

	if s.endswith('tri'):
		if nacin == 0: #primer: trije milijoni
			tmp = 'je'
		else: #primer: tri milijarde
			tmp = '' 
		return (s + tmp, 'tri')

	if s.endswith('štiri'):
		if nacin == 0: #primer: štirje milijoni
			tmp = 'je'
		else: #primer: štiri milijarde
			tmp = 'i' 
		return (s[:-1] + tmp, 'štiri')

	return (s, 'difolt')

def to_num_dont_call(x):
	ilijon = ['ilijon', 'ilijona', 'ilijoni', 'ilijonov']
	ilijarda = ['ilijarda', 'ilijardi', 'ilijarde', 'ilijard']
	koncnice = list(zip(ilijon, ilijarda))
	predpone = ['m', 'b', 'tr', 'kvadr', 'kvint', 'sekst', 'sept', 'okt', 'non', 'dec', 'undec', 'duodec', 'tredec']

	#stevilo = razporedi_po_tri(x)
	stevilo = x

	r = []
	r.append(do1e6(stevilo % 1000_000))
	stevilo //= 1000_000


	sklon = {'ena':0, 'dva':1, 'tri':2, 'štiri':2, 'difolt':3} # .get('stevilka', default = 3)
	stikalo = 0
	count = 0
	while stevilo > 0:
		tmp = do1000(stevilo % 1000)
		tmp, konec = sklanjaj(tmp, stikalo)

		if tmp != '':
			tmp += '-' + predpone[count] + koncnice[sklon[konec]][stikalo] #izbere med ilijoni in ilijardami, pravo šrevilo; sestavi zapis
			r.append(tmp)
		stikalo = (stikalo + 1) % 2 #stikalo: 1 -> 0; 0 -> 1 (ilijarda -> ilijon; ilijon -> ilijarda)
		stevilo //= 1000

		if stevilo > 0:
			tmp = do1000(stevilo % 1000)
			tmp, konec = sklanjaj(tmp, stikalo)

			if tmp != '':		
				tmp += '-' + predpone[count] + koncnice[sklon[konec]][stikalo] #izbere med ilijoni in ilijardami, pravo šrevilo
				r.append(tmp)
		stikalo = (stikalo + 1) % 2 #stikalo: 1 -> 0; 0 -> 1 (ilijarda -> ilijon; ilijon -> ilijarda)
		stevilo //= 1000
		count += 1	
	r.reverse()
	return	filtriraj_minuse('-'.join(r))


decimalke = lambda x: ['nula', 'ena', 'dva', 'tri', 'štiri', 'pet', 'šest', 'sedem', 'osem', 'devet'][x]

def to_decimal(s):
	r='-cela'
	for x in s:
		r += '-' + decimalke(int(x))
	return r

def filtriraj_minuse(s): #minuse na začetku in če je kakšen podvojen in na koncu odstranim
	tmp = [x for x in s.split('-') if x != '']
	return '-'.join(tmp)


def to_num(x):
	if type(x) == str:
		celi_del = int(x.split('.')[0])
	else:
		celi_del=int(x)
	
	################ če je nič na začetku
	if celi_del == 0:
		prvi_del = 'nič'
	else:
		prvi_del = to_num_dont_call(abs(celi_del))

	################ predznak
	if '-' in str(x):
		predznak='minus-'
	else:
		predznak=''

	################# decimalke
	if '.' in str(x) and not 'e' in str(x): #zapisa 1.4e+20 program ni zmožen obdelati
		drugi_del = to_decimal(str(x).split('.')[1])
	else:
		drugi_del = ''

	r= prvi_del + drugi_del #sestavim del pred piko + del za piko

	############### če so na koncu minusi, jih odrežem
	if len(r) > 0:
		if r[-1] == '-':
			return predznak+r[:-1]

	return predznak+r


########################################### v tem delu se generirajo deli števil npr sto = 100, pet = 5 ...
stevila = {}
for x in range(100):
	stevila[to_num(x)] = x
for x in range(1, 10):
	stevila[to_num(100*x)] = 100*x

deset_na = {}
for x in range(1,28):
	for d in range(5):
		stevila[to_num((100 + d)*1000**x).split('-')[-1]] = 1000**x
		deset_na[to_num((100 + d)*1000**x).split('-')[-1]] = 1000**x

stevila['nula']=0
stevila['štirje']=4
stevila['trije']=3
stevila['dve']=2
stevila['en']=1
##########################################
def from_num(x):
	if type(x) in [int, float]:
		return x
	a=x.split('-') # razbijem na posamezne besede
	################### urejanje predznaka
	z=a.pop(0)
	if z=='minus':
		predznak = -1
	else:
		a.insert(0, z)
		predznak = 1
	###################
	r=0
	stack = []
	decimalke = False
	vrednost_decimalke = 1/10
	for y in a:
		if y in deset_na.keys(): #če je beseda za desetiško potenco pomnoži s prejšnim delom in prišteje rezultatu
			if len(stack) > 0:
				pre = stack.pop()
			else:
				pre=1
			r+=stevila[y]*pre

		elif decimalke: # če je to decimalka prištevamo kot decimalko
			r+=vrednost_decimalke*stevila[y]
			vrednost_decimalke /= 10

		elif y in stevila.keys(): # če ni decimalka in ni desetiška potenca, potem je sprednji del primer: 132 165 sprednja dela bosta 132 in 165, pomnožena s 1000 in 1
			if len(stack) > 0:
				pre = stack.pop()
			else:
				pre=0
			stack.append(stevila[y]+pre)

		elif y == 'cela': # znak za decimalno vejico, od tu naprej so samo še decimalke
			decimalke = True
			if stack != []:
				r+=stack.pop()
		

	if stack != []: # če česa še ni prištel naredi to zdaj
		r+=stack.pop()
	return r*predznak # vrne vrednost s pravim predznakom

def test():
	for _ in range(20):
		a=input('napiši število z besedo ali ne: ')
		try:
			a=int(a)
			print(to_num(a))
		except:
			print(from_num(a))

if __name__ == '__main__':
	#test()
	pass