import os
import time
from datetime import datetime, timezone

from controllers import FILE
from controllers import API
from controllers import UTILS
from controllers import DISCORD

def start():
    gather_stats = FILE.get_json("data/gather_stats.json")
    print(gather_stats)
    current_datetime = datetime.now(timezone.utc)
    session_seconds = 0

    if "last_ran" not in gather_stats:
        gather_stats["last_ran"] = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        last_ran = current_datetime
    else:
        last_ran = datetime.strptime(gather_stats["last_ran"], "%Y-%m-%d %H:%M:%S")

    print("[GATHER]: Starting to gather data")
    print(f"   |Date:  {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}")
    print(f"   |Last Ran:  {gather_stats["last_ran"]}")
    print(f"   |Seconds / Call:  {gather_stats['seconds_per_call']}\n")

    DISCORD.send_gather_start(current_datetime.strftime("%Y-%m-%d %H:%M:%S"), gather_stats)

    gather_stats["last_ran"] = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    FILE.write_json(gather_stats,"../data/gather_stats.json","w")

    running = True
    last_updated = None
    while running:
        hours = session_seconds // 3600
        minutes = (session_seconds % 3600) // 60
        seconds = session_seconds % 60

        gather_stats["session_duration"] = f"{hours:02}:{minutes:02}:{seconds:02}"

        if session_seconds % 15 == 0:
            UTILS.create_skyfetch_img(gather_stats)
            DISCORD.send_gather_img()

        session_seconds += gather_stats['seconds_per_call']


        market_data = API.get_current_market_data()
        market_data_time = datetime.fromtimestamp(market_data["lastUpdated"] / 1000)

        print("[GATHER]:")
        print(f"   |Data Last Updated:  {market_data_time}\n")

        gather_stats["session_api_calls"] += 1
        gather_stats["hourly_api_calls"] += 1

        if last_updated  != market_data["lastUpdated"]:
            last_updated = market_data_time
            year, month, day = market_data_time.isocalendar()
            folder_path = f"output/{year}/{month}/{day}"

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            write_time = int(time.time())
            UTILS.write_remove_enchants(market_data,f"{folder_path}/{write_time}.json")
            FILE.compress(f"{folder_path}/{write_time}")

            print("[GATHER]:")
            print(f"   |Market Data logged at:  {write_time}\n")


        time.sleep(gather_stats['seconds_per_call'])