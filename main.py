from datetime import datetime, timezone, timedelta

from controllers import API

# Fetch market data
# API.update_market_data()
market_dict = API.get_data()



print(f"[Update Time]: {(datetime.fromtimestamp(market_dict['lastUpdated'] / 1000 , tz=timezone.utc) + timedelta(hours=-7)).strftime('%Y-%m-%d %H:%M:%S MST')}")

products = market_dict['products']

max_imabalance = [float('-inf'),""]
min_imabalance = [float('inf'),""]

for contract_id in products:

    contract = products[contract_id]
    if "ENCHANTMENT" in contract['product_id']:
        continue

    total_orders = contract['quick_status']['buyVolume'] + contract['quick_status']['sellVolume']
    order_difference = contract['quick_status']['buyVolume'] - contract['quick_status']['sellVolume']
    imabalance = None if total_orders == 0 else order_difference / total_orders

    print(f"[{contract['product_id']} Imbalance]: {imabalance}]")

    if None != imabalance > max_imabalance[0] :
        max_imabalance[0] = imabalance
        max_imabalance[1] = contract['product_id']

    if None != imabalance < min_imabalance[0]:
        min_imabalance[0] = imabalance
        min_imabalance[1] = contract['product_id']


print(f"[Max Imbalanced Contract]: {max_imabalance[1]} | {max_imabalance[0]}")
print(f"[Min Imbalanced Contract]: {min_imabalance[1]} | {min_imabalance[0]}")