import itertools

def seqbin(k):
	return [''.join(x) for x in itertools.product("01", repeat=k)]

def dectobin (dec):
	return bin(dec)

def bintodec (binary):
	return int(str(binary),2)


try:
	while True:
		N = raw_input()
except EOFError:
	pass