from googlefinance import getQuotes
import json

stocks = ["BABA", "AAPL", "GOOG"]

#print(getQuotes(stocks))

stock_data = getQuotes(stocks)

for stock in stock_data:
	print("The price of {} is: ${}".format(stock['StockSymbol'],stock['LastTradePrice']))