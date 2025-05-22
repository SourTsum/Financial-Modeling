import pandas as pd
import ast
import math

file = 'data/drop_chance_tables/mob_drops.csv'

df = pd.read_csv(file)

def drop_chance(item, magic_find, pet_luck, farming_fortune, crop_fortune):
    if item not in df['Drop'].values:
        return -1

    drop = df[df['Drop'] == item]
    percent_strs = ast.literal_eval(drop['Chance'].values[0])
    mob_strs = ast.literal_eval(drop['Mob'].values[0])
    location_strs = ast.literal_eval(drop['Location'].values[0])

    chances = [float(p.strip('%')) for p in percent_strs]
    best_indeces = [i for i, chance in enumerate(chances) if chance == max(chances)]
    base_chance = max(chances)
    best_mobs = [mob_strs[i] for i in best_indeces]
    best_locations = [location_strs[i] for i in best_indeces]

    print(f"Base chance for {item} is {base_chance}% from {', '.join(best_mobs)}\n")

    best_chances = []

    for i in range(len(best_mobs)):
        chance = base_chance
        if drop['Type'].values[0] == 'Pet':
            if location_strs[i] == 'Garden':
                chance *= 1 + (pet_luck + farming_fortune + crop_fortune) / 600
            else:
                chance *= 1 + (pet_luck + magic_find) / 100
        else:
            if location_strs[i] == 'Garden':
                chance *= 1 + (farming_fortune + crop_fortune) / 600
            else:
                chance *= 1 + magic_find / 100

        best_chances.append(chance)

    best_chance = max(best_chances)
    best_mobs = [best_mobs[i] for i in range(len(best_chances)) if best_chances[i] == best_chance]
    best_locations = [best_locations[i] for i in range(len(best_chances)) if best_chances[i] == best_chance]

    print(f"Best chance for {item} is {best_chance}% from {', '.join(best_mobs)} in {', '.join(best_locations)}\n")

    return best_chance

def chance_in_trials(chance, drops):
    chance /= 100
    prob = 1 - (1 - chance) ** drops
    print(f"Chance of getting at least one drop in {drops} trials: {round(prob * 100, 2)}%\n")

    return prob

def trials_for_probability(chance, desired):
    chance /= 100
    desired /= 100

    if chance <= 0 or desired >= 1:
        return float('inf')

    n = math.log(1 - desired) / math.log(1 - chance)
    print(f"To reach {desired * 100}% chance with {chance * 100}% drop rate, you need ~{math.ceil(n)} trials.\n")
    return math.ceil(n)

print('\033c')

best_chance = drop_chance("EPIC Scatha Pet", 122, 83, 354.8, 0)
chance_in_trials(best_chance, 127)
trials_for_probability(best_chance, 50)