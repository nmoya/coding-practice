 # Given a string that contain parentheses (), check if they are balanced.

def balanced(string):
	stack = []
	for letter in string:
		if letter == '(':
			stack.append(letter)
		elif letter == ')':
 			if len(stack) > 0:
 				top = stack.pop()
 				if top != '(':
	 				return False
	 		else:
	 			return False
	return len(stack) == 0

if __name__ == '__main__':
 	print balanced("(())")		# True
 	print balanced("(()())")	# True
 	print balanced("()(()())")	# True
 	print balanced("(()")		# False
 	print balanced("))")		# False



