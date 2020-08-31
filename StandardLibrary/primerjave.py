try:
    from StandardLibrary.bulVar import BUL
except:
    from bulVar import BUL

def enako(sklad):
	sklad.append(BUL(sklad.pop() == sklad.pop()))

def isto(sklad):
    sklad.append(BUL(sklad.pop() is sklad.pop()))

def manjše(sklad):
    sklad.append(BUL(sklad.pop() < sklad.pop()))

def večje(sklad):
    sklad.append(BUL(sklad.pop() > sklad.pop()))

def ne(sklad):
    sklad.append(BUL(sklad.pop() - BUL('Da')))

primerjave = {'3':enako, '9':isto, '7':manjše, '2':večje, '5':ne}