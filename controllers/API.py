from controllers import FILE
import requests

def update_market_data():
    market_data = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    FILE.write_json(market_data.json(),'./output/market_data.json')

def get_data():
    try:

        return FILE.get_json('./output/market_data.json')
    except Exception as e:
        with open("./output/logs.txt", "w") as logging:
            logging.write(str(e))
        print(f"[API Controller]: full_data file doesn't exist OR can't read from file...")