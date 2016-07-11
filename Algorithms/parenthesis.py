 # Given a string that contain parentheses only `(` and `)`, check if the parenthesis are balanced.

def balanced(string):
	stack = []
	for letter in string:
		if letter == '(':
			stack.append(letter)
		elif letter == ')':
 			if len(stack) > 0:
 				stack.pop()
	 		else:
	 			return False
	return len(stack) == 0

if __name__ == '__main__':
 	assert(balanced("(())"))
 	assert(balanced("(()())"))
 	assert(balanced("()(()())"))
 	assert(balanced("(()") == False)
 	assert(balanced("))") == False)



