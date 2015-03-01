import math


def under_attack((x1, y1), (x2, y2)):
	return (x1 == x2) or (y1 == y2) or (math.fabs(x2-x1) == math.fabs(y2-y1))


solutions = []
def solve_queens(N, nbr_queens, q_positions):
	if nbr_queens == 0:
		global solutions
		solutions.append(q_positions)
	else:
		for i in range(N):
			inSight = False
			currentRow = (N - nbr_queens)
			if currentRow == 0:
				solve_queens(N, nbr_queens-1, q_positions + [(currentRow, i)])
			else:
				for queen in q_positions:
					if under_attack((currentRow, i), queen):
						inSight = True
						break
				if not inSight:
					solve_queens(N, nbr_queens-1, q_positions + [(currentRow, i)])


if __name__ == "__main__":
	solve_queens(10, 10, [])
	print len(solutions)


