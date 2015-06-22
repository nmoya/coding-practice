import math
# - Find duplicate in positive integer array of size N, every integer in range (1, N-1) appears at least once.
def find_duplicates(arr):
	duplicates = []
	for i, number in enumerate(arr):
		index = int(math.fabs(arr[i]))
		if arr[index] >= 0:
			arr[index] = -arr[index]
		else:
			duplicates.append(int(math.fabs(arr[i])))
	arr = map(math.fabs, arr)
	arr = map(int, arr)
	return duplicates

# Given an array which may contain duplicates, return a new array with only one occurrence of the elements
def unique(arr):
	new_arr = []
	_hash = dict()
	for el in arr:
		_hash[el] = 1
	for key in _hash:
		new_arr.append(key)
	return new_arr

if __name__ == '__main__':
	print find_duplicates([1, 2, 3, 1, 3, 6, 6])
	print unique([1, 2, 3, 1, 3, 6, 6])