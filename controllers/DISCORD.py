import os
import requests
from dotenv import load_dotenv

load_dotenv("data/hidden.env")

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
if not WEBHOOK_URL:
    raise ValueError("DISCORD_WEBHOOK_URL not found in .env file")

def send_error(message):
    embed = {
        "embeds": [{
            "title": "[GATHER]: Error",
            "description": message,
            "color": 16711680  # Red
        }]
    }

    response = requests.post(WEBHOOK_URL, json=embed)

    if response.status_code != 204:
        print(f"Failed to send error: {response.status_code}, {response.text}")
    else:
        print("[DISCORD]: Successfully sent error to Discord")


def send_gather_start(current_datetime, start_stats):
    embed = {
        "embeds": [{
            "title": "🟢 [GATHER]: Started",
            "color": 3066993,  # Green
            "fields": [
                {
                    "name": "Date",
                    "value": current_datetime,
                    "inline": False
                },
                {
                    "name": "Last Ran",
                    "value": start_stats.get("last_ran", "N/A"),
                    "inline": True
                },
                {
                    "name": "Seconds / Call",
                    "value": str(start_stats.get("seconds_per_call", "N/A")),
                    "inline": True
                }
            ]
        }]
    }

    response = requests.post(WEBHOOK_URL, json=embed)

    if response.status_code != 204:
        print(f"Failed to send gather_stats: {response.status_code}, {response.text}")

def send_gather_stats(write_time,last_updated):
    embed = {
        "embeds": [{
            "title": "[GATHER]: Data Saved",
            "color": 3447003,  # Blue
            "fields": [
                {
                    "name": "File Timestamp",
                    "value": str(write_time),
                    "inline": False
                },
                {
                    "name": "API Last Updated",
                    "value": str(last_updated),
                    "inline": True
                }
            ]
        }]
    }

    response = requests.post(WEBHOOK_URL, json=embed)

    if response.status_code != 204:
        print(f"Failed to send gather_stats update: {response.status_code}, {response.text}")