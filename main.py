from itertools import combinations

from controllers import FILE
import pandas as pd

election_results = pd.read_csv('data/election_results.csv')

mayor = FILE.get_json("./output/mayor_data.json")
current_mayor , current_minister = mayor["mayor"]["name"] , mayor["mayor"]["minister"]["name"]

# gets active candidates
candidates = ["Aatrox", "Diana", "Paul", "Marina", "Cole", "Foxy", "Finnegan", "Diaz"]
active_candidates = candidates.copy()
active_candidates.remove(current_mayor)
active_candidates.remove(current_minister if current_minister != "Diaz" else None)

for thing in list(combinations(active_candidates, 5)):
    print(list(thing))