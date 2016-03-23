import random

REVERSE_BIASED_SAMPLE_COUNT = 1000
SAMPLE_SIZE = 1000000

player_1_options = ['R', 'P', 'S']
player_2_options = ['P', 'S'] + ['R']*REVERSE_BIASED_SAMPLE_COUNT

score_map = {
    'RS': 1,
    'RP': -1,
    'PR': 1,
    'PS': -1,
    'SP': 1,
    'SR': -1
}

def choose_winner(player_1_value, player_2_value):
    output = 0
    if (player_1_value!=player_2_value):
        output = score_map[player_1_value+player_2_value]
    return output


if __name__ == "__main__":
    total_score = 0
    for sample in range(SAMPLE_SIZE):
        total_score = total_score + choose_winner(random.choice(player_1_options),
                                                  random.choice(player_2_options))
    print(total_score)