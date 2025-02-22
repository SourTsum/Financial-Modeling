from controllers import FILE
import pandas as pd

election_stats = FILE.get_json("./data/election_stats.json")
election_results = pd.read_csv("./data/election_results.csv")
current_election = FILE.get_json("./output/mayor_data.json")

class Mayor():
    def __init__(self, name):
        self.name = name
        self.perks = []





def generate_perk_prediction():
    current_mayor = current_election["mayor"]["name"]
