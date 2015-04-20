from __future__ import division
import sys
import random


def rand_without_repetition(_min, _max, n):
	if (_max - _min)+1 >= n:
		tmp = range(_min, _max+1, 1)
		random.shuffle(tmp)
		return tmp[:n]
	else:
		print "Invalid interval or number of samples"
		sys.exit(-1)


class Matrix():
	def __init__(self, xsize, ysize):
		self.xsize = xsize
		self.ysize = ysize
		self.data = []
		for i in range(xsize):
			self.data.append([0]*ysize)

	def __repr__(self):
		output = ''
		for line in self.data:
			output += "   ".join(map(str, line)) + "\n"
		return output

	def transpose(self):
		tmp = zip(*self.data)
		for i in range(self.ysize):
			self.set_row(i, list(tmp[i]))

	def set_row(self, row, array):
		if row < self.ysize:
			self.data[row] = array
		else:
			print "Invalid row in set row. Row %d Ysize %d" % (row, self.ysize)
			sys.exit(-1)

	def set_middle(self, value):
		self.data[int(self.xsize/2)][int(self.ysize/2)] = value


class Ticket():
	def __init__(self, size, max_value):
		self.size = size
		self.max_value = max_value
		self.ticket = Matrix(size, size)
		self.gen_ticket()
		self.ticket.set_middle(-1)
		
		self.label  = Matrix(size, size)
		self.label.set_middle(1)

	def __repr__(self):
		matrix = self.ticket.__repr__()
		lbl    = self.label.__repr__()
		matrix = matrix.split("\n")
		lbl    = lbl.split("\n")
		output = ""
		for i in range(len(matrix)-1):
			output += "\t\t".join([matrix[i], lbl[i]]) + "\n"
		return output

	def clear(self):
		self.label = Matrix(self.size, self.size)
		self.label.set_middle(1)

	def gen_ticket(self):
		step = int(self.max_value / self.size)
		for i in range(self.ticket.ysize):
			# print (i*step)+1, (i*step)+step, self.size
			self.ticket.set_row(i, rand_without_repetition((i*step)+1,
														   (i*step)+step,
														   self.size))
		self.ticket.transpose()

	def mark_number(self, number):
		for i in range(self.ticket.ysize):
			for j in range(self.ticket.xsize):
				if self.ticket.data[i][j] == number:
					self.label.data[i][j] = 1
					return

	def check_ticket(self, win_condition):
		if win_condition == "Row":
			for row in self.label.data:
				if sum(row) == self.size:
					return True
			return False
		elif win_condition == "Column":
			self.label.transpose()
			for row in self.label.data:
				if sum(row) == self.size:
					self.label.transpose()
					return True
			self.label.transpose()
			return False
		elif win_condition == "Diagonal":
			_sum = 0
			for i in range(self.label.ysize):
				_sum += self.label.data[i][i]
			if _sum == self.size:
				return True
			else:
				return False
		elif win_condition == "Both_Diagonals":
			_sum1 = 0
			_sum2 = 0
			for i in range(self.label.ysize):
				_sum1 += self.label.data[i][i]
				_sum2 += self.label.data[i]\
										[self.label.ysize-(i+1)]
			if _sum1 == self.size and _sum2 == self.size:
				return True
			else:
				return False
		elif win_condition == "Full":
			_sum = 0
			for line in self.label.data:
				_sum += sum(line)
			if _sum == self.size ** 2:
				return True
			else:
				return False


class Player():
	def __init__(self, _id, nbr_tickets, ticket_size, max_value):
		self.id = _id
		self.wins = 0
		self.nbr_tickets = nbr_tickets
		self.tickets = []
		for i in range(nbr_tickets):
			self.tickets.append(Ticket(ticket_size, max_value))

	def __repr__(self):
		output = "Player # %d\n" % (self.id)
		output += "Tickets: %d \t Wins: %d\n" % (self.nbr_tickets, self.wins)
		return output

	def hear_number(self, win_condition, number):
		winner = False
		for t in self.tickets:
			t.mark_number(number)
			winner = winner or t.check_ticket(win_condition)
		return winner


	def clear(self):
		for t in self.tickets:
			t.clear()


class Event():
	def __init__(self, **kargs):
		self.id                         = kargs.get("id", 1)
		self.win_condition              = kargs.get("win_condition", "Row")
		self.ticket_size                = kargs.get("ticket_size", 5)
		self.max_value                  = kargs.get("max_value", 75)
		self.nbr_players                = kargs.get("nbr_players", 30)
		self.nbr_tickets_sp_player 		= kargs.get("nbr_tickets_sp_player", 10)
		self.avg_tickets_per_player     = kargs.get("avg_tickets_per_player", 2)
		self.nbr_rounds                 = kargs.get("nbr_rounds", 30)

		self.players = []
		self.players.append(Player(1, self.nbr_tickets_sp_player,
							self.ticket_size, self.max_value))
		for i in range(2, self.nbr_players):
			self.players.append(Player(i+2, self.avg_tickets_per_player,
								self.ticket_size, self.max_value))

		self.winner = self.players[0]

	def __repr__(self):
		output = "Event # %d\n" % (self.id)
		output += "Players: %d  Winner ID: %d\n" % (self.nbr_players,
														self.winner.id)
		output += "Won %d of %d rounds." % (self.winner.wins, self.nbr_rounds)
		return output

	def tiebreak(self, round_winners):
		tie_break = rand_without_repetition(1, self.max_value,
											len(round_winners))
		_max = max(tie_break)
		_max_idx = -1
		for idx, num in enumerate(tie_break):
			if num == _max:
				_max_idx = idx
				break
		return round_winners[idx]

	def simulate(self):
		special_player_won = False
		avg_wins = 0
		for rnd in range(self.nbr_rounds):
			numbers = rand_without_repetition(1, self.max_value,
											  self.max_value)
			round_winners = []
			for numb in numbers:
				for p in self.players:
					if p.hear_number(self.win_condition, numb):
						round_winners.append(p)
				if len(round_winners) != 0:
					round_winner = self.tiebreak(round_winners)
					round_winner.wins += 1
					if round_winner.wins > self.winner.wins:
						self.winner = round_winner
					break
			for player in self.players:
				player.clear()

		if self.winner.id == 1:
			special_player_won = True

		return special_player_won, self.players[0].wins
		# print self
		# sorted_players=sorted(self.players,reverse=True,key=lambda p: p.wins)
		# for p in sorted_players:
		# 	if p.wins != 0:
		# 		print "Player # %d: %f" % (p.id, p.wins / self.nbr_rounds)



if __name__ == "__main__":
	wins = 0
	rounds = 0
	win_conditions = ["Row", "Column", "Diagonal", "Both_Diagonals", "Full"]
	number_of_events = 100
	nbr_rounds = 15
	for i in range(1, number_of_events+1):
		if i % 10 == 0:
			print "Simulating event # %d" % (i)
		e = Event(id=i, win_condition=random.choice(win_conditions),
				  nbr_players=50, nbr_tickets_sp_player=50,
				  avg_tickets_per_player=1, nbr_rounds=nbr_rounds)

		aux_wins, aux_rounds = e.simulate()
		if aux_wins:
			wins += 1
		rounds += aux_rounds

	print "-----------------------------------------"
	print "Special player was first place in %.2f p" % ((wins/number_of_events) * 100)
	print "Change to win a round: %.2f p" % ((rounds / (number_of_events * nbr_rounds)) *100)
	print "Expected to win %.2f rounds of %d" % (rounds / number_of_events, nbr_rounds)
	print "-----------------------------------------"

