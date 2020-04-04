from code.service.intraday.get_us_intraday import stock_us_price_intraday
from code.service.ticker.get_us_ticker_list import save_us_data, get_us_tickers
import time

save_us_data()
tickers = get_us_tickers()
for i, ticker in enumerate(tickers):
    try:
        print('Intraday', ticker, i, '/', len(tickers))
        stock_us_price_intraday(ticker, folder="../../data/IntradayUS")
        time.sleep(2)
    except:
        pass
    if i > 3:
        break
print("US-Intraday for all stocks got.")
