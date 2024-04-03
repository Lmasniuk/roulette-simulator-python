%matplotlib inline
import matplotlib.pyplot as plt

import random

sequence_bets = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 7,
    8: 10,
    9: 14,
    10: 20,
    11: 28,
    12: 39,
    13: 55,
    14: 76,
}

TOTAL_SPINS = 200
AVG_SPIN_TIME = 3
NUMBERS_PLAYED = 10
RESET_POINT = 2

winning_results = []

def play_games():
    wins = 0
    losses = 0
    bet = 1

    money = 0

    for x in range(0, TOTAL_SPINS):
        outcome = random.randint(1, 38)
        if (outcome in range(1,NUMBERS_PLAYED+1)):
            wins = wins + 1
            winnings = (35 * sequence_bets[bet]) - (sequence_bets[bet] * NUMBERS_PLAYED )
            money = money + winnings
            bet = 1
        else:
            losses = losses + 1
            money = money - (sequence_bets[bet] * NUMBERS_PLAYED)
            if(bet == RESET_POINT):
                bet = 1
            else:
                bet = bet + 1
        winning_results.append(money)
    return winning_results

results = play_games() 

print('Final Earnings: $' + str(results[-1]))

plt.plot(results)
plt.ylabel('Earnings')
plt.show()