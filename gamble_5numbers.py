%matplotlib inline
import matplotlib.pyplot as plt

import random

sequence_bets = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 2,
    8: 2,
    9: 3,
    10: 3,
    11: 4,
    12: 4,
    13: 5,
    14: 6,
    15: 7,
    16: 8,
    17: 9,
    18: 11,
    19: 13,
    20: 15,
    21: 17,
    22: 20,
    23: 24,
    24: 28,
    25: 32,
    26: 38,
    27: 44,
    28: 51
}

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

TOTAL_SPINS = 100000
NUMBERS_PLAYED = 5

RESET_POINT = 20

winning_results = []
results = play_games() 

print('Final Earnings: $' + str(results[-1]))

plt.plot(results)
plt.ylabel('Earnings')
plt.show()