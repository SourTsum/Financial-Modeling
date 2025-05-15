import pandas as pd

file = 'data/drop_chance_tables/kills_bracket.csv'

df = pd.read_csv(file)

def clean_number(val):
    if isinstance(val, str):
        val = val.replace(',', '')
        if val.isdigit():
            return int(val)
    return val

df = df.applymap(clean_number)

df.to_csv(file, index=False)