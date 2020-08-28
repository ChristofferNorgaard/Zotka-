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