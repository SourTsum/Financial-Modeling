from controllers import FILE

import json
from PIL import Image, ImageFont, ImageDraw

def write_remove_enchants(market_data,file_path):
    """

    :param market_data:
    :param file_path:
    :return:
    """



    FILE.write_text("{", file_path, "w")
    FILE.write_text('"success": ' + str(market_data["success"]).lower() + ",\n", file_path, "a")
    FILE.write_text('"lastUpdated": ' + str(market_data["lastUpdated"]) + ",\n", file_path, "a")
    FILE.write_text('"products": {',file_path, "a")

    market_products = market_data['products']



    first_pass = True
    for product in market_products:
        if "ENCHANTMENT" not in product:
            if first_pass:
                FILE.write_text(f'"{product}" : ' + f"{json.dumps(market_products[product])}", file_path, "a")
                first_pass = False
            else:
                FILE.write_text(",\n", file_path, "a")
                FILE.write_text(f'"{product}" : ' + f"{json.dumps(market_products[product])}", file_path, "a")

    FILE.write_text('}}', file_path, "a")


font = ImageFont.truetype("arialbd.ttf", 55)

def create_skyfetch_img(gather_stats):
    SkyFetchIMG = Image.open("data/SkyFetch.png")
    draw = ImageDraw.Draw(SkyFetchIMG)

    x_offset , y_offset = 5250, 335
    draw_data = {
        "hourly_api_calls" : {
            "data" : str(gather_stats["hourly_api_calls"]),
            "position" : (x_offset,0 + y_offset),
        },
        "hourly_data_written" : {
            "data" : str(gather_stats["hourly_data"]) + " MB",
            "position" : (x_offset,82 + y_offset)
        },
        "session_api_calls": {
            "data" : str(gather_stats["session_api_calls"]),
            "position" : (x_offset,315 + y_offset)
        },
        "session_data_written": {
            "data" : str(gather_stats["session_data"])  + " GB",
            "position" : (x_offset,400 + y_offset)
        },
        "session_time" : {
            "data" :  str(gather_stats["session_duration"]),
            "position" : (x_offset,480 + y_offset)
        }
    }

    for i , item in enumerate(draw_data):
        draw.text(
            draw_data[item]["position"],
            draw_data[item]["data"],
            "white",
            font=font
        )
    SkyFetchIMG.save("output/SkyFetch.png")