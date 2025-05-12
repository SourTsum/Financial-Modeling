from controllers import FILE
import requests


def get_current_market_data():
    """
    requests the skyblock/bazaar API
    """
    market_data = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    return market_data.json()


def get_cached_market_data():
    try:
        return FILE.get_json('./output/original_market_data.json')
    except Exception as e:
        with open("./output/logs.txt", "w") as logging:
            logging.write(str(e))
        print("[API Controller]: market_data file doesn't exist OR can't read from file...")

def get_current_mayor_data():
    market_data = requests.get("https://api.hypixel.net/v2/resources/skyblock/election")
    FILE.write_json(market_data.json(),'./output/mayor_data.json')