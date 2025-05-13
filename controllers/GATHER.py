import os
import time
from datetime import datetime, timezone

from controllers import FILE
from controllers import API
from controllers import UTILS
from controllers import DISCORD

def start():
    start_stats = FILE.get_json("../data/gather_stats.json")
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    print("[GATHER]: Starting to gather data")
    print(f"   |Date:  {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}")
    print(f"   |Last Ran:  {start_stats["last_ran"]}")
    print(f"   |Seconds / Call:  {start_stats['seconds_per_call']}\n")

    DISCORD.send_gather_stat(current_datetime, start_stats)

    start_stats["last_ran"] = current_datetime
    FILE.write_json(start_stats,"../data/gather_stats.json","w")

    running = True
    last_updated = None
    while running:
        market_data = API.get_current_market_data()

        market_data_time = datetime.fromtimestamp(market_data["lastUpdated"] / 1000)

        print("[GATHER]:")
        print(f"   |Data Last Updated:  {market_data_time}\n")

        if last_updated  != market_data["lastUpdated"]:

            year, month, day = market_data_time.isocalendar()
            folder_path = f"output/{year}/{month}/{day}"

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            write_time = int(time.time())
            UTILS.write_remove_enchants(market_data,f"{folder_path}/{write_time}.json")
            FILE.compress(f"{folder_path}/{write_time}")



        time.sleep(start_stats['seconds_per_call'])