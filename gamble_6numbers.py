%matplotlib inline
import matplotlib.pyplot as plt

import random

sequence_bets = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 4,
    10: 5,
    11: 6,
    12: 7,
    13: 8,
    14: 10,
    15: 12,
    16: 15,
    17: 18,
    18: 22,
    19: 26,
    20: 31,
    21: 38,
    22: 46
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

TOTAL_SPINS = 200
NUMBERS_PLAYED = 6

RESET_POINT = 2

winning_results = []
results = play_games() 

print('Final Earnings: $' + str(results[-1]))

plt.plot(results)
plt.ylabel('Earnings')
plt.show()