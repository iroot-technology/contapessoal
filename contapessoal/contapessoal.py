import yfinance as yf

stock = yf.Ticker("WEGE3.SA")

print(stock.info)
