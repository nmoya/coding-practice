def power(base, pow):
	if pow == 1:
		return base
	elif pow % 2 == 0:
		return power(base, pow/2) * power(base, pow/2)
	else:
		return base * power(base, pow-1)


print power(2, 10)
print power(2, 3)
print power(5, 3)