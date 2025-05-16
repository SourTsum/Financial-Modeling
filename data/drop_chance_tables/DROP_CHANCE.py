import pandas as pd

file = 'data/drop_chance_tables/kills_bracket.csv'

#df = pd.read_csv(file)

def drop_chance(magic_find : float, farming_fortune : float, pet_luck : float, drop_chance : float, useFarmingFortune : bool) -> float:
    if not useFarmingFortune: return drop_chance * (1 + (magic_find + pet_luck) / 100)
    else: return drop_chance * (1 + (magic_find + pet_luck) / 100)