# import alpaca_trade_api as tradeapi
# import time

# # Replace with your Alpaca API key and secret
# API_KEY = 'your_api_key'
# API_SECRET = 'your_api_secret'
# BASE_URL = 'https://paper-api.alpaca.markets'

# # Initialize Alpaca API
# api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL, api_version='v2')

# # Define trading parameters
# symbol = 'AAPL'
# quantity = 1
# buy_price = 150.0
# sell_price = 160.0

# # Main trading loop
# while True:
#     # Get the current price
#     current_price = api.get_latest_trade(symbol).price

#     # Buy if the current price is below the buy price
#     if current_price < buy_price:
#         print(f"Buying {quantity} shares of {symbol} at {current_price}")
#         api.submit_order(
#             symbol=symbol,
#             qty=quantity,
#             side='buy',
#             type='limit',
#             time_in_force='gtc',
#             limit_price=current_price
#         )

#     # Sell if the current price is above the sell price
#     elif current_price > sell_price:
#         print(f"Selling {quantity} shares of {symbol} at {current_price}")
#         api.submit_order(
#             symbol=symbol,
#             qty=quantity,
#             side='sell',
#             type='limit',
#             time_in_force='gtc',
#             limit_price=current_price
#         )

#     # Sleep for a minute before checking again
#     time.sleep(60)
