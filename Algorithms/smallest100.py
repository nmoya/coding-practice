import heapq

def smallest_10_inefficient(array):
	h = []
	for value in array:
		heapq.heappush(h, value)

	output = []
	for i in range(10):
		output.append(heapq.heappop(h))
	return output

def smallest_numbers(array, numbers):
	h = array[::]
	heapq.heapify(h)

	output = []
	for i in range(numbers):
		output.append(heapq.heappop(h))
	return output


if __name__ == '__main__':
	arq = open("./cpp/hundred")
	content = arq.read().split("\n")
	content = map(int, content)
	arr = smallest_numbers(content, 10)
	print arr