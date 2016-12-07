import sys
st=[]

def tobinary(x):
	if (x>0):
		return ('0'*(8-len(bin(x).split('b')[1]))+bin(x).split('b')[1])
	else:
		rep = ''.join(map(str,[str(1-int(i)) for i in ('0'*(8-len(bin(abs(x)).split('b')[1]))+bin(abs(x)).split('b')[1]) ]))
		x = int(rep, 2)+1
		return ('0'*(8-len(bin(x).split('b')[1]))+bin(x).split('b')[1])


def fractionalPartToBinary(x):
	start = x
	ans=''
	for i in range(23):

	 	x=x*2
	 	# print(x)
	 	if x>=1:
	 		ans+='1'
	 		x-=1
	 	else:
	 		ans+='0'
	return ans
def rep(x):
	px = x
	x = abs(x)
	bias=0
	if x!=0:
		while (x<1):
			x*=2
			bias-=1
		while (x>2):
			x/=2
			bias+=1

		x-=1
	return "{0} {1} {2}".format(('1' if px<0 else '0'), tobinary(126+1+bias), fractionalPartToBinary(x))


def out():
	if (len(st)==0):
		print("empty")
	for (pos, val) in enumerate(st):
		print("ST{0}: {1} [{2}]".format(pos, rep(val), val))

def load(x):
	x = float(x)
	if len(st)>0:
		st.insert(0, x)
	else:
		st.append(x)
def add():
	st[1]+=st[0]

def mul():
	st[1]*=st[0]

def sub():
	st[1]-=st[0]

def div():
	st[1]/=st[0]

def exch():
	st[0], st[1] = st[1], st[0]

def dubl():
	st.append(st[0])

def pop():
	st.pop(0)

def check(x):
	if (len(x)>2):
		return ValueError
	if x[0] not in ['load', 'div', 'mul', 'pop', 'add', 'sub', 'exch', 'dubl', 'exit']:
		raise ValueError
	if (x[0]!='load' and len(x)>1):
		raise ValueError
	if (x[0]=='load' and len(x)!=2):
		raise ValueError

def makeOperation(x):
	if (x[0]=='load'):
		load(x[1])
	elif (x[0]=='exit'):
		raise SystemExit
	else:
		(globals()[x[0]]())
	

while 1:
	out()
	command = input('>').split(' ')
	try:
		check(command)
		makeOperation(command)
	except SystemExit:
		break
	except:
		print('Wrong command')

