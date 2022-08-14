import yfinance as yf


def get_price(symbol):
    symbol = symbol.upper()
    ticker = yf.Ticker(symbol)
    return "The current stock price of " + ticker.info['shortName'] + " is: $" + str(ticker.info['currentPrice'])
