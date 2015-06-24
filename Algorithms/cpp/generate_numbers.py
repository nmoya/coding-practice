import random
import sys

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "python generate_numbers.py output amount"
		sys.exit(-1)

	output = sys.argv[1]
	amount = int(sys.argv[2])
	rand = []
	for i in range(amount):
		rand.append(random.randint(0, 1000000))

	rand = map(str, rand)
	arq = open(output, "w")
	arq.write("\n".join(rand))
	arq.close()