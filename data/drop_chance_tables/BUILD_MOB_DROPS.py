import pandas as pd
import ast

file = "data/drop_chance_tables/mob_drops.csv"

def write_to_dataframe(df, drop_name, mob_name, drop_chance, mob_location, item_type):
    if drop_name not in df['Drop'].values:
        new_row = pd.DataFrame({
            'Drop': [drop_name],
            'Mob': [[mob_name]],
            'Chance': [[drop_chance]],
            'Location': [[mob_location]],
            'Type': [item_type]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file, index=False)
    else:
        idx = df[df['Drop'] == drop_name].index[0]
        mob_list = ast.literal_eval(df.at[idx, 'Mob'])
        chance_list = ast.literal_eval(df.at[idx, 'Chance'])
        loc_list = ast.literal_eval(df.at[idx, 'Location'])
        mob_list.append(mob_name)
        chance_list.append(drop_chance)
        loc_list.append(mob_location)
        df.at[idx, 'Mob'] = str(mob_list)
        df.at[idx, 'Chance'] = str(chance_list)
        df.at[idx, 'Location'] = str(loc_list)
        df.to_csv(file, index=False)


while True:
    print('\033c')
    df = pd.read_csv(file)
    print("Enter the name of the drop: ")
    drop_name = input()
    print("\nEnter the name of the mob: ")
    mob_name = input()
    print("\nEnter the drop chance: ")
    drop_chance = input()
    print("\nEnter the location of the mob: ")
    mob_location = input()
    print("\nEnter the dropped item type (Item, Pet, Accessory, Dye, Enchanted Book): ")
    item_type = input()
    write_to_dataframe(df, drop_name, mob_name, drop_chance, mob_location, item_type)