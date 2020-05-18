def to_num_dont_call(x):
	x=int(x)
	if x == 0:
		return('')
	c=len(list(str(x)))
	num=['','ena','dva','tri','štiri','pet','šest','sedem','osem','devet']

	if c==1:
		tmp=['ena','dva','tri','štiri','pet','šest','sedem','osem','devet']
		return(str(tmp[x-1]))

	elif c==2:
		y=[int(str(x)[0]),int(str(x)[1])]
		if x<20:
			tmp=['deset','enajst','dvanajst','trinajst','štirinajst','petnajst','šestnajst','sedemnajst','osemnajst','devetnajst']
			return(tmp[y[1]])
		if x==20:
			return('dvajset')

		r1=num[y[1]]
		if y[1] > 0:
			r1+='in'
		if y[0]==2:
			r2=num[y[0]]+'jset'
		else:
			r2=num[y[0]]+'deset'
		return(r1+r2)

	elif c==3:
		if x == 100:
			return('sto')
		else:
			y=[x//100,x%100]
			tmp=['','dve','tri','štiri','pet','šest','sedem','osem','devet']
			return(tmp[y[0]-1]+'sto-'+to_num_dont_call(y[1]))
	elif c==4:
		y=x//1000
		tmp=['','dva-','tri-','štiri-','pet-','šest-','sedem-','osem-','devet-']
		return(tmp[y-1]+'tisoč-'+to_num_dont_call(x%1000))
	elif c<7:
		y=x//1000
		tmp=['deset','enajst','dvanajst','trinajst','štirinajst','petnajst','šestnajst','sedemnajst','osemnajst','devetnajst']
		return(to_num_dont_call(y)+'-tisoč-'+to_num_dont_call(x%1000))
	elif c<10:
			if x//1000000%100==1:
				return(to_num_dont_call(x//1000000)[0:-1] +'-milijon-'+to_num_dont_call(x%1000000))
			elif x//1000000%100==2:
				return(to_num_dont_call(x//1000000) +'-milijona-'+to_num_dont_call(x%1000000))
			if x//1000000%100 in [3,4]:
				return(to_num_dont_call(x//1000000) + '-milijone-'+to_num_dont_call(x%1000000))
			else:
				return(to_num_dont_call(x//1000000) + '-milijonov-'+to_num_dont_call(x%1000000))
	elif x==1000000000:
		return('ena-milijarda')
	elif x>1000000000:
		if x//int(1e9)%100==1:
			tmp = to_num_dont_call(int(x//1e9))[0:-1] 
			if tmp[-3:]=='dva':
				tmp=tmp[:-3]+'dve'
			if tmp[-2:]=='en':
				tmp=tmp[:-2]+'ena'
			tmp += '-milijarda-'+to_num_dont_call(x%1e9)
			return tmp
		elif x//1e9%100==2:
			tmp = to_num_dont_call(x//1e9) 
			if tmp[-3:]=='dva':
				tmp=tmp[:-3]+'dve'
			if tmp[-2:]=='en':
				tmp=tmp[:-2]+'ena'
			tmp += '-milijardi-'+to_num_dont_call(x%1e9)
			return tmp
		if x//1e9%100 in [3,4]:
			tmp = to_num_dont_call(x//1e9) 
			if tmp[-3:]=='dva':
				tmp=tmp[:-3]+'dve'
			if tmp[-2:]=='en':
				tmp=tmp[:-2]+'ena'
			tmp += '-milijarde-'+to_num_dont_call(x%1e9)
			return tmp
		else:
			tmp = to_num_dont_call(x//1e9) 
			if tmp[-3:]=='dva':
				tmp=tmp[:-3]+'dve'
			if tmp[-2:]=='en':
				tmp=tmp[:-2]+'ena'			
			tmp += '-milijard-'+to_num_dont_call(x%1e9)
			return tmp

def to_num(x):
	if x < 0:
		predznak='minus-'
	else:
		predznak=''
	r=to_num_dont_call(abs(x))
	if len(r) > 0:
		if r[-1] == '-':
			return predznak+r[:-1]
	return predznak+r

stevila = {}
for x in range(100):
	stevila[to_num(x)] = x
for x in range(1, 10):
	stevila[to_num(100*x)] = 100*x
ccc=['tisoč', 'milijona', 'milijon', 'milijone', 'milijonov', 'milijarda', 'milijardi', 'milijarde', 'milijard']
cccv=[1000, 1000000, 1000000, 1000000, 1000000, 1000000000, 1000000000, 1000000000, 1000000000]
for x in range(len(ccc)):
	stevila[ccc[x]] = cccv[x]
stevila['en']=1


def from_num(x):
	a=x.split('-')
	z=a.pop(0)
	if z=='minus':
		predznak = -1
	else:
		a.insert(0, z)
		predznak = 1
	#print(a)
	r=0
	stack = []
	for y in a:
		if y in ['tisoč', 'milijona', 'milijon', 'milijone', 'milijonov', 'milijarda', 'milijardi', 'milijarde', 'milijard']:
			if len(stack) > 0:
				pre = stack.pop()
			else:
				pre=1
			r+=stevila[y]*pre
		else:
			if len(stack) > 0:
				pre = stack.pop()
			else:
				pre=0
			stack.append(stevila[y]+pre)
	if stack != []:
		r+=stack.pop()
	return r*predznak

def test():
	for x in range(20):
		a=input('napiši število z besedo ali ne: ')
		try:
			a=int(a)
			print(to_num(a))
		except:
			print(from_num(a))

if __name__ == '__main__':
	test()