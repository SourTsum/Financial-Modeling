from controllers import API
from controllers import FILE

import json

def write_remove_enchants(market_data,file_path):
    """

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
