import sys


def nbr_change_possibilities(amount, coins):

    coins_given_amount = [0] * (amount + 1)
    coins_given_amount[0] = 1

    for value in range(amount):

        for coin in coins:

            if coin <= value:

                remaining_value = value - coin
                coins_given_amount[value] += coins_given_amount[remaining_value]

    return coins_given_amount[amount - 1]


def min_nbr_of_coins(amount, coins):
    coins_given_amount = [sys.maxint] * (amount + 1)
    coins_given_amount[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                remaining_value = value - coin
                current = coins_given_amount[remaining_value] + 1

                coins_given_amount[value] = min(current,
                                                coins_given_amount[value])

    return coins_given_amount[amount]


print nbr_change_possibilities(11, [1, 3, 5])
print nbr_change_possibilities(5, [1, 3, 5])
print nbr_change_possibilities(50, [1, 5, 10, 25, 50])

print min_nbr_of_coins(11, [1, 3, 5])
